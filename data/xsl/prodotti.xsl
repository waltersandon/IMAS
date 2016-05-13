<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:pr="http://imas.it/xml/xsd/prodotti">

<xsl:template match="/pr:catalogo">
<div id="container">
<xsl:for-each select="pr:categoria">
<div class="categoria">
	<img class="circolare fotocat" src="{pr:fotocat}" alt="{pr:altcat}" />
	<div class="testocat">
	<h1><xsl:value-of select="pr:nomecat" /><a href="#top" class="tothetop">[torna su]</a></h1>
	<p><xsl:value-of select="pr:descrcat" /></p>
	</div>
</div>
<xsl:for-each select="pr:prodotto">
<div class="prodotto">
	<img class="circolare fotoprod" src="{pr:foto}" alt="{pr:alt}" />
	<div class="testoprod">
	<h2><xsl:value-of select="pr:nomeprod" /></h2>
	<p><xsl:value-of select="pr:descrizione" /></p>
	<p>Lavorazioni disponibili:</p>
		<ul class="ullav">
		<xsl:for-each select="pr:lavorazione">
		<xsl:if test="text()='Verniciatura'">
		<li><img class="circolare fotolav" src="../public_html/images/verniciatura.jpg" alt="Verniciatura" />
		<p>Verniciatura</p></li>
		</xsl:if>
		<xsl:if test="text()='Cromatura'">
		<li><img class="circolare fotolav" src="../public_html/images/cromatura.jpeg" alt="Cromatura" />
		<p>Cromatura</p></li>
		</xsl:if>
		<xsl:if test="text()='Taglio'">
		<li><img class="circolare fotolav" src="../public_html/images/taglio.jpg" alt="Taglio" />
		<p>Taglio</p></li>
		</xsl:if>
		</xsl:for-each>
		</ul>
	</div>
</div>
</xsl:for-each>

</xsl:for-each>
</div>

</xsl:template>

</xsl:stylesheet>
