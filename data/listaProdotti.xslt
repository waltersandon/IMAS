<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fm="http://www.imas.it" exclude-result-prefixes="fm">
<xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'
doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" />

<xsl:template match="/" >
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<title>Imas s.n.c.</title>
<meta name="title" content="Lavorazione e piegatura di fili metallici" />
<meta name="description" content="Homepage del sito di Antonio Basso Imas" />
<meta name="keywords" content="ganci, griglie, filo metallico, cromatura, griglie per forni, griglie per stufe" />
<meta name="language" content="italian it" />
<meta name="author" content="Walter Sandon" />
<link href="../home.css" rel="stylesheet" type="text/css" />
</head>
<body>

<div id="header">
<a href="home.html" id="logoCirc" title="Logo aziendale Imas"></a>
<div id="headerfloat"><a id="logoenome" href="../struttura.html">Imas S.n.c.</a>
<p id="sottologo">di Speggiorin Fausto &amp; Co.</p>
</div>

</div>

<div id="subheader">
<p id="fblogo" class="socials"><a href="https://www.facebook.com/profile.php?id=1198179612" title="Logo Facebook"></a></p>
<img id="panoramic" src="images/panoramic.jpg" alt="Foto panoramica dell'azienda Imas" />
</div>
  
<div id="tabs">
<ul id="ultabs">
<li id="lihome" class="selected navtab"><span>Home</span></li>
<li id="liprod" class="notselected navtab"><a href="prodotti.html">Prodotti</a></li>
<li id="lilav" class="notselected navtab"><a href="lavorazioni.html">Lavorazioni</a></li>
<li id="licont" class="notselected navtab"><a href="contatti.html">Contatti</a></li>
</ul>
</div>

<div id="container">

<div id="path">
Ti trovi nella sezione: Home <img class="pathicon" src="icons/home_icon.png" alt="Icona Home"></img>
</div>

<div id="nav">
<h1>Contenuti:</h1>
<ul id="listnav">
<li>&gt;<a href="#chisiamo">Chi siamo?</a></li>
<li>&gt;<a href="#cosaprod">Cosa produciamo?</a></li>
<li>&gt;<a href="#lastoria">La nostra storia</a></li>
</ul>
</div>
 
<div id="content"> 
<xsl:for-each select="fm:prodotti/fm:prodotto">
  <h1><xsl:value-of select="fm:titolo/fm:prefazione"/> <span> PER</span> 
    <xsl:for-each select="fm:titolo/fm:segmento">
      <xsl:if test="@number>1">, </xsl:if>
      <xsl:value-of select="."/>
    </xsl:for-each>
</h1>
<p><xsl:value-of select="fm:descrizione"/></p>
</xsl:for-each>
<h1><a name="chisiamo">Chi siamo?</a></h1>
<p>La Griglie Srl un'azienda specializzata nel fabbricare griglie ed altre cose in ferro ed acciaio.</p>
<p>In attività nel Veneto fin dal 1562, vanta un'enorme esperienza ed affidabilità nel suo settore.</p>
<p>Oltre alla vendita dei suoi prodotti tipo griglie, la Griglie Srl offre svariati servizi di lavorazione di altre cose.</p>
<p>Per contattarci si clicchi <a href="contatti.html">qui</a> o si visiti la sezione "Contatti".</p>
<h1><a name="cosaprod">Cosa produciamo?</a></h1>
<p>La nostra produzione consiste specialmente in affari di ferro utilizzati a livello industriale in tutto il mondo. I nostri prodotti più famosi sono la griglia grandezza media e la grata modello 2, per i quali abbiamo ottenuto un premio d'eccellenza all'<a href="http://www.expo2015.org/">Expo Milano 2015</a>.</p>
<p>Oltre alla produzione industriale, fabbrichiamo anche alcuni prodotti domestici come lo spago di ferro sottile.</p>
<p>Per il catalogo completo dei nostri prodotti, si clicchi <a href="prodotti.html">qui</a> o si visiti la sezione "Prodotti".</p>
<p>I nostri metodi di lavorazione prevedono principalmente la verniciatura coi pennelli, antiruggine e fosforescente.</p>
<p>Per conto di terzi offriamo anche l'arrotino per le griglie.</p>
<p>Per ulteriori informazioni sui nostri metodi di lavorazione, si clicchi <a href="lavorazioni.html">qui</a> o si visiti la sezione "Lavorazioni".</p>
<h1><a name="lastoria">La nostra storia</a></h1>
<p>Griglie Srl, venne fondata nel 1555 da un tizio che non aveva niente di meglio da fare.</p>
<p>Da quel giorno Griglie Srl si è occupata di fabbricare griglie e robe metalliche per anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni</p>
<p>Ed anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni.</p> <p>Ed anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni.</p>
<p>Ed anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni.</p>
<p>Ed anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni.</p>
<p>Ed anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni e anni.</p>
<p>E tutto questo è vero ancora fino ad oggi.</p>
</div>

</div>
<div id="footer">
<span><a href="http://validator.w3.org/check?uri=referer"><img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a></span>
<span><a href="http://jigsaw.w3.org/css-validator/check/referer"><img style="border:0;width:88px;height:31px" src="http://jigsaw.w3.org/css-validator/images/vcss-blue" alt="CSS Valido!" /></a></span>
<span class="footerinfostart">Imas S.n.c.</span>
<span class="footerinfo">Via della Saldatura 55, Valferro(TV)</span>
<span class="footerinfo">Tel: 0455-5566556</span>
</div>
</body>
</html>
</xsl:template>       
</xsl:stylesheet>