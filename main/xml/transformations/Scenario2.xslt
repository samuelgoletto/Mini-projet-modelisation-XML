<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8"/>

    <xsl:template match="/">
        <html>
            <head>
                <title>Liste des intervenants parlant allemand</title>
                <link rel="stylesheet" type="text/css" href="../output1.css"/>
            </head>
            <body>
                <h1>Liste des intervenants parlant allemand</h1>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Nom</th>
                        <th>Prénom</th>
                        <th>Âge</th>
                        <th>Langues parlées</th>
                    </tr>
                    <xsl:apply-templates select="sejours-linguistiques/intervenants/intervenant[langues/langue='allemand']"/>
                </table>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="intervenant">
        <tr>
            <td><xsl:value-of select="@id"/></td>
            <td><xsl:value-of select="nom"/></td>
            <td><xsl:value-of select="prenom"/></td>
            <td><xsl:value-of select="age"/></td>
            <td><xsl:apply-templates select="langues"/></td>
        </tr>
    </xsl:template>

    <xsl:template match="langues">
        <xsl:for-each select="langue">
            <xsl:value-of select="."/><xsl:if test="position() != last()">, </xsl:if>
        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>
