#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

checkSession();

my $cgi = new CGI;

$fileXMLprod = $fileXMLProdotti;
$fileXMLlav = $fileXMLLavorazioni;

my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($fileXMLprod);
my $radice = $doc->getDocumentElement;
my @categoria = $radice->getElementsByTagName('categoria');

my $parserlav = XML::LibXML->new();
my $doclav = $parserlav->parse_file($fileXMLlav);
my $radicelav = $doclav->getDocumentElement;
my @nomelav = $radicelav->getElementsByTagName('nomeLav');

printHTML("../public_html/parts/insprod_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/insprod_nav.xhtml");

print "<!-- Start Container -->
<div id='container' class='lightgrey'>
<form action='../cgi-bin/insprod_result.cgi' method='post' enctype='multipart/form-data'>
<p class='warning marginleft'>Per inserire un nuovo prodotto, compilare i campi dati sottostanti:</p>";

my @ids = $radice->getElementsByTagName('id');
my $maxid = 1;
foreach $ids(@ids) {
	$idstring = $ids->string_value;
	$idcode = substr $idstring, 2;
	if($idcode > $maxid) { $maxid = $idcode; }
}
$maxid += 1;
$maxid = "ID".$maxid;

print "<ul class='ulnopadd formmargin'>
<li><input type='hidden' name='id' id='id' value='$maxid' /></li>
<li><label for='selectcateg'>Categoria: </label>
<select tabindex='11' id='selectcateg' name='selectcateg' class='formmargin'>";

foreach $categoria(@categoria) {
	my $listacat = $categoria->getElementsByTagName('nomecat')->string_value;
	print "<option>$listacat</option>";
}

print "</select></li>
<li><label for='nomeprod'>Nome Prodotto: </label><input tabindex='12' type='text' id='nomeprod' name='nomeprod' class='formmargin' /></li>
<li><label for='foto'>Foto: </label><input tabindex='13' type='file' id='foto' name='foto' class='formmargin' /></li>
<li><label for='alt'>Alt: </label><input tabindex='14' type='text' id='alt' name='alt' class='formmargin' /></li>
<li>Lavorazioni disponibili:";

my $tabindex = 15;

foreach $nomelav(@nomelav) {
	my $listalav = $nomelav->string_value;
	print "<p class='standardcheckb'><input tabindex='$tabindex' type='checkbox' id='check$listalav' name='check$listalav' value='$listalav' /><label for='check$listalav'>$listalav</label></p>";
	$tabindex += 1;
}

print "</li>
<li><p id='ptexta2'><label for='texta2'>Descrizione:</label></p>
<textarea tabindex='$tabindex' id='texta2' name='texta2' rows='0' cols='0'></textarea></li>
</ul>";

$tabindex += 1;

print "<p><input tabindex='$tabindex' type='submit' value='Inserisci Prodotto' class='submit' /></p>
</form>
</div>";

printFOOTER();
printBODY_END();
printHTML_END();
