<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" omit-xml-declaration="yes"/>

    <xsl:template match="/catalogo">
        <div id="container">
            <xsl:for-each select="categoria">
			<xsl:sort select="nomecat" />
                <xsl:variable name="tab" select = "position()+10"/>
                <xsl:if test="position() mod 2 = 0">
                    <div class="pari">
                        <div class="catContent">
                            <img class="circolare fotocat" src="{fotocat}" alt="{altcat}" />
                            <div class="testocat">
                                <h1><xsl:value-of select="nomecat" /><a href="#top" class="tothetop" tabindex="{$tab+1}">[torna su]</a>
                                </h1>
                                <p><xsl:value-of select="descrcat" /></p>
                            </div>
                        </div>
                        <xsl:for-each select="prodotto">
						<xsl:sort select="nomeprod" />
                            <div class="circleGrid">
                                <img class="circolare fotoprod" src="{foto}" alt="{alt}"/>
                                <h1><xsl:value-of select="descrizione"/></h1>
                                <xsl:for-each select="lavorazione">
								<xsl:sort select="." />
                                    <p class='elencolav'><xsl:value-of select="."/></p>
                                </xsl:for-each>
                            </div>
                        </xsl:for-each>
                    </div>
                </xsl:if>
                <xsl:if test="position() mod 2 != 0">
                    <div class="dispari">
                        <div class="catContent">
                            <img class="circolare fotocat" src="{fotocat}" alt="{altcat}" />
                            <div class="testocat">
                                <h1><xsl:value-of select="nomecat" /><a href="#top" class="tothetop" tabindex="{$tab}">[torna su]</a>
                                </h1>
                                <p><xsl:value-of select="descrcat" /></p>
                            </div>
                        </div>
                        <xsl:for-each select="prodotto">
						<xsl:sort select="nomeprod" />
                            <div class="circleGrid">
                                    <img class="circolare fotoprod" src="{foto}" alt="{alt}"/>
                                    <h1><xsl:value-of select="descrizione"/></h1>
                                    <xsl:for-each select="lavorazione">
									<xsl:sort select="." />
                                        <p class='elencolav'><xsl:value-of select="."/></p>
                                    </xsl:for-each>
                            </div>
                        </xsl:for-each>
                    </div>
                </xsl:if>
            </xsl:for-each>
        </div>
    </xsl:template>
</xsl:stylesheet>
