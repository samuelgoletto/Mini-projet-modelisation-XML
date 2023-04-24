<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/">
        <xsl:element name="sejours-linguistiques">
            <xsl:element name="sejours">
                <xsl:for-each select="//sejour">
                    <xsl:element name="sejour">
                        <xsl:copy-of select="type"/>
                        <xsl:copy-of select="nom"/>
                        <xsl:copy-of select="public"/>
                        <xsl:copy-of select="langues"/>
                        <xsl:copy-of select="destination"/>
                        <xsl:copy-of select="prix"/>
                    </xsl:element>
                </xsl:for-each>
            </xsl:element>
        </xsl:element>
    </xsl:template>
</xsl:stylesheet>