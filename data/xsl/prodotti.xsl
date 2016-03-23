<?xml version="1.0"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:pr="http://imas.it/xml/xsd/prodotti">

<xsl:template match="/pr:catalogo">
<html><body>
<h1>Catalogo prodotti</h1>
<xsl:for-each select="pr:categoria">
<h2><xsl:value-of select="pr:nomecat" /></h2>
<xsl:for-each select="pr:prodotto">
<p><xsl:value-of select="pr:nomeprod" /></p>
<p><xsl:value-of select="pr:categoria" /></p>
<p><xsl:value-of select="pr:descrizione" /></p>
<p><xsl:value-of select="pr:lavorazione" /></p>
</xsl:for-each>
</body></html>
</xsl:template>

</xsl:stylesheet>