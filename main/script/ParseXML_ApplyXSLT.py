from platform import system as os_core_name
from os import system as cmd
from glob import iglob as files_gen
from os.path import abspath, isdir, isfile
from os import mkdir


YES = 'yes', 'y', 'ok'
NO = 'no', 'n'
path = {
		'xml': '../xml/*',
		'xml_doc': '../xml/ExtraitSejourLinguistique.xml',
		'xml_schema': '../xml/SejourLinguistique.xsd',
		'xml_transformations': '../XML/transformations/*',
		'output': '../xml/transfo_output/*',

		'json': '../json/*',
		'json_doc': '../json/ExtraitSejourLinguistique.json',
		'json_schema': '../json/Schema.json'
	}



def EXIT():
	input('Press <Enter> to exit')
	exit()
def GET_FILE_NAME(path):
	return '.'.join(abspath(path).replace('\\', '/').split('/')[-1].split('.')[:-1])
def QUESTION(txt = ''):
	print(txt)
	print('[yes (y), no (n)]')
	input_ = input('>>> ').lower()
	while input_ not in (YES + NO):
		input_ = input('>>> ').lower()
	return input in YES



def apply_transformations(xml_doc, trees, output_files_names, output_folder = None):
	if type(trees) == etree._ElementTree:
		trees = trees,

	if output_folder == None:
		result = ()
	else:
		if output_folder.endswith('*'):
			output_folder = output_folder[:-1]
		if isfile(output_folder):
			print(f'Cannot output to "{output_folder}" as it is not a directory'); EXIT()
		elif not isdir(output_folder):
			mkdir(output_folder)
		output_folder = abspath(output_folder)
		if not output_folder.endswith('/'):
			output_folder += '/'


	for t, output_file_name in zip(trees, output_files_names):
		transformator = etree.XSLT(t)
		output = etree.tostring(transformator(xml_doc), pretty_print = True) # binary
		# print('transform with etree._ElementTree.xslt:', root.xslt(t))

		if output_folder == None:
			result += output,
		else:
			output_full_path = output_folder + output_file_name + '.html'
			with open(output_full_path, 'wb') as file:
				file.write(output)
			print(f'File "{output_full_path}" has been overwritten')


	if output_folder == None:
		return result

def import_setup():

	try:
		import lxml
		del lxml
	except ModuleNotFoundError:
		pass
	else:
		return True

	commands = 'python3 -m pip install lxml', 'python -m pip install lxml'

	for mod_dl_cmd in commands:
		if cmd(mod_dl_cmd) == 0: # If download successful
			break
	else:
		print('Unable to download lxml with python pip module\nTrying to download pip')
		install_pip()

	return False



def import_xml_files(path = path['xml']):
	result = ()

	for x in (files_gen(path) if path.endswith('*') else (path,)):
		try:
			xml_tree = etree.parse(x)
		except etree.XMLSyntaxError as exc:
			print(f'Please fix this Syntax Error in file {x}:')
			print('\t', exc)
		except etree.XMLSchemaParseError as exc:
			print(f'Please fix this Parsing Error in file {x}:')
			print('\t', exc)
		except Exception as exc:
			print(f'{type(exc)} error caught in file {x}:')
			print('\t', exc)
		else:
			result += xml_tree,


	if len(result) == 0:
		return None
	elif len(result) == 1:
		return result[0]
	else:
		return result



def install_pip():
	osCoreName = os_core_name()
	if osCoreName == 'Linux':
		pip_install_commands = 'sudo apt update --fix-missing', 'sudo apt install python3-pip', # tuple, please let the dam comma, thx
		print('Please provide your password to allow python pip (package manager) to be installed')
	elif osCoreName == 'Windows':
		pip_install_commands = 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py', 'python get-pip.py'
	else:
		print('Unknown OS'); EXIT()

	for c in pip_install_commands:
		if cmd(c) != 0:
			print('Unable to download python pip.\nThis program will terminate'); EXIT()



def validate_with(xml_doc, schema):
	xml_validator = etree.XMLSchema(schema)
	return xml_validator.validate(xml_doc)
	# print('validate method 2 with etree._ElementTree.xmlschema:', root.xmlschema(schema))



## Setup ##
if not import_setup():
	print('Please re-run this program to acknowledge updates in modules'); EXIT()
from lxml import etree
###########


if __name__ == '__main__':



	print('\n' + '='*32)
	print(f'''Parsing XML files in "{path['xml']}"\nApplying XSLT from "{path['xml_transformations']}"''')
	print('\nPress <Ctrl> + <C> to exit at any moment')
	print(32*'=' + '\n')



	## Retrieve files ##
	root = import_xml_files(path['xml_doc'])
	root_name = GET_FILE_NAME(path['xml_doc'])
	schema = import_xml_files(path['xml_schema'])
	schema_name = GET_FILE_NAME(path['xml_schema'])
	transformations = import_xml_files(path['xml_transformations'])
	transformations_names = tuple(GET_FILE_NAME(f) for f in files_gen(path['xml_transformations']))
	####################


	## Validation & transformations ##
	if validate_with(root, schema):
		print(f'''Xml file "{path['xml_doc']}" correctly satisfies the requirements specified in schema "{path['xml_schema']}"''')
	else:
		print(f'''Xml file "{path['xml_doc']}" does not satisfies the requirements specified in schema "{path['xml_schema']}"'''); EXIT()
		if not QUESTION('Continue with transformations anyway?'):
			EXIT()


	apply_transformations(root, transformations, output_files_names = transformations_names, output_folder = path['output'])
	##################################



	EXIT()
