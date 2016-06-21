<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:pr="http://imas.it/xml/xsd/prodotti">

    <xsl:template match="/pr:catalogo">
        <div id="container">
            <xsl:for-each select="pr:categoria">
                <xsl:variable name="tab" select = "position()+10"/>
                <xsl:if test="position() mod 2 = 0">
                    <div class="pari">
                        <div class="catContent">
                            <img class="circolare fotocat" src="{pr:fotocat}" alt="{pr:altcat}" />
                            <div class="testocat">
                                <h1><xsl:value-of select="pr:nomecat" /><a href="#top" class="tothetop" tabindex="{$tab+1}">[torna su]</a>
                                </h1>
                                <p><xsl:value-of select="pr:descrcat" /></p>
                            </div>
                        </div>
                        <xsl:for-each select="pr:prodotto">
                            <div class="circleGrid">
                                <ul>
                                    <li><img class="circolare fotoprod" src="{pr:foto}" alt="{pr:alt}"/></li>
                                    <li><h2><xsl:value-of select="pr:descrizione"/></h2></li>
                                    <xsl:for-each select="pr:lavorazione">
                                        <li><p><xsl:value-of select="."/></p></li>
                                    </xsl:for-each>
                                </ul>
                            </div>
                        </xsl:for-each>
                    </div>
                </xsl:if>
                <xsl:if test="position() mod 2 != 0">
                    <div class="dispari">
                        <div class="catContent">
                            <img class="circolare fotocat" src="{pr:fotocat}" alt="{pr:altcat}" />
                            <div class="testocat">
                                <h1><xsl:value-of select="pr:nomecat" /><a href="#top" class="tothetop" tabindex="{$tab}">[torna su]</a>
                                </h1>
                                <p><xsl:value-of select="pr:descrcat" /></p>
                            </div>
                        </div>
                        <xsl:for-each select="pr:prodotto">
                            <div class="circleGrid">
                                    <img class="circolare fotoprod" src="{pr:foto}" alt="{pr:alt}"/>
                                    <h2><xsl:value-of select="pr:descrizione"/></h2>
                                    <xsl:for-each select="pr:lavorazione">
                                        <p><xsl:value-of select="."/></p>
                                    </xsl:for-each>
                            </div>
                        </xsl:for-each>
                    </div>
                </xsl:if>
            </xsl:for-each>
        </div>
    </xsl:template>
</xsl:stylesheet>
