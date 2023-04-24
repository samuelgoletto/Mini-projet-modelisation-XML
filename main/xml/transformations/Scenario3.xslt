<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>Activités du séjour</title>
      </head>
      <body>
        <h1>Activités du séjour "Immersion au coeur de Londres"</h1>
        <xsl:apply-templates select="sejours-linguistiques/sejours/sejour[nom='Immersion au coeur de Londres']/activites/activite"/>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="activite">
    <li><xsl:value-of select="nom"/> (Jour <xsl:value-of select="jour"/>)</li>
  </xsl:template>

</xsl:stylesheet>
