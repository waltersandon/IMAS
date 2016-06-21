<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:lv="http://imas.it/xml/xsd/lavorazioni">
  
  <xsl:template match="/lv:lavorazioni">
    <div id="container">
      <xsl:for-each select="lv:lavorazione">
          <xsl:variable name="tab" select = "position()+10"/>
        <xsl:if test="position() mod 2 = 0">
          <div class="dispari">
            <div class="fotoL">
              <img class="circolare" src="{lv:fotoLav}" alt="{lv:nomeLav}"/>
            </div>
            <div class="testoL">
              <h1><xsl:value-of select="lv:nomeLav"/><a href="#top" class="tothetop" tabindex="{$tab+1}">[torna su]</a></h1>
              <h2>Produzione <xsl:value-of select="@produzione"/></h2>
              <p><xsl:value-of select="lv:descrLav"/></p>
              <xsl:for-each select="lv:commento">
                <p><xsl:value-of select="."/></p>
              </xsl:for-each>
            </div>
          </div>
        </xsl:if>
        <xsl:if test="position() mod 2!=0">
            <div class="pari">
                <div class="fotoL">
                    <img class="circolare" src="{lv:fotoLav}" alt="{lv:nomeLav}"/>
                </div>
                <div class="testoL">
                    <h1><xsl:value-of select="lv:nomeLav"/><a href="#top" class="tothetop" tabindex="{$tab+1}">[torna su]</a></h1>
                    <h2>Produzione <xsl:value-of select="@produzione"/></h2>
                    <p><xsl:value-of select="lv:descrLav"/></p>
                    <xsl:for-each select="lv:commento">
                        <p><xsl:value-of select="."/></p>
                    </xsl:for-each>
                </div>
            </div>
      </xsl:if>
      </xsl:for-each>
    </div>
  </xsl:template>

</xsl:stylesheet>
