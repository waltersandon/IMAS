<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/catalogo">
<div id="container">
<xsl:for-each select="categoria">
<div class="categoria">
	<img class="circolare fotocat" src="{fotocat}" alt="{altcat}" />
	<div class="testocat">
	<h1><xsl:value-of select="nomecat" /><a href="#top" class="tothetop">[torna su]</a></h1>
	<p><xsl:value-of select="descrcat" /></p>
	</div>
</div>
<xsl:for-each select="prodotto">
<div class="prodotto">
	<img class="circolare fotoprod" src="{foto}" alt="{alt}" />
	<div class="testoprod">
	<h2><xsl:value-of select="nomeprod" /></h2>
	<p><xsl:value-of select="descrizione" /></p>
	<p>Lavorazioni disponibili:</p>
		<ul class="ullav">
		<xsl:for-each select="lavorazione">
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
