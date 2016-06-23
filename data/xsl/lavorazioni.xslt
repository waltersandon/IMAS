<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSl/Transform">
  
  <xsl:template match="/lavorazioni">
    <div id="container">
      <xsl:for-each select="lavorazione">
          <xsl:variable name="tab" select = "position()+10"/>
        <xsl:if test="position() mod 2 = 0">
          <div class="dispari">
            <div class="fotol">
              <img class="circolare" src="{fotolav}" alt="{altlav}"/>
            </div>
            <div class="testol">
              <h1><xsl:value-of select="nomelav"/><a href="#top" class="tothetop" tabindex="{$tab+1}">[torna su]</a></h1>
              <h2>Produzione <xsl:value-of select="@produzione"/></h2>
              <p><xsl:value-of select="descrlav"/></p>
              <xsl:for-each select="commento">
                <p><xsl:value-of select="."/></p>
              </xsl:for-each>
            </div>
          </div>
        </xsl:if>
        <xsl:if test="position() mod 2!=0">
            <div class="pari">
                <div class="fotol">
                    <img class="circolare" src="{fotolav}" alt="{altlav}"/>
                </div>
                <div class="testol">
                    <h1><xsl:value-of select="nomelav"/><a href="#top" class="tothetop" tabindex="{$tab}">[torna su]</a></h1>
                    <h2>Produzione <xsl:value-of select="@produzione"/></h2>
                    <p><xsl:value-of select="descrlav"/></p>
                    <xsl:for-each select="commento">
                        <p><xsl:value-of select="."/></p>
                    </xsl:for-each>
                </div>
            </div>
      </xsl:if>
      </xsl:for-each>
    </div>
  </xsl:template>

</xsl:stylesheet>
