<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <head>
                <link rel="stylesheet" type="text/css" href="output1.css"/>
                <title>Sejours destinés aux enfants</title>
            </head>
            <body>
                <h1>Sejours destinés aux enfants</h1>
                <table>
                    <tr>
                        <th>Nom</th>
                        <th>Destination</th>
                        <th>Prix</th>
                    </tr>
                    <xsl:for-each select="sejours-linguistiques/sejours/sejour[public='enfants']">
                        <tr>
                            <td><xsl:value-of select="nom"/></td>
                            <td><xsl:value-of select="destination"/></td>
                            <td><xsl:value-of select="prix"/>€</td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
