<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:lv="http://imas.it/xml/xsd/lavorazioni">
  
  <xsl:template match="/lv:lavorazioni">
    <div id="container">
      <xsl:for-each select="lv:lavorazione">
        <xsl:if test="position() mod 2 = 0">
          <div class="dispari">
            <div class="foto">
              <img class="circolare" src="{lv:fotoLav}" alt="{lv:nomeLav}"/>
            </div>
            <div class="testo">
              <h1><xsl:value-of select="lv:nomeLav"/><a href="#top" class="tothetop">[torna su]</a></h1>
              <h2>Produzione <xsl:value-of select="@produzione"/></h2>
              <p><xsl:value-of select="lv:descrizione"/></p>
              <xsl:for-each select="lv:commento">
                <p><xsl:value-of select="."/></p>
              </xsl:for-each>
            </div>
          </div>
        </xsl:if>
        <xsl:if test="position() mod 2!=0">
            <div class="pari">
                <div class="foto">
                    <img class="circolare" src="{lv:fotoLav}" alt="{lv:nomeLav}"/>
                </div>
                <div class="testo">
                    <h1><xsl:value-of select="lv:nomeLav"/><a href="#top" class="tothetop">[torna su]</a></h1>
                    <h2>Produzione <xsl:value-of select="@produzione"/></h2>
                    <p><xsl:value-of select="lv:descrizione"/></p>
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
