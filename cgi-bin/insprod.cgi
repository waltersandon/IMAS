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
<div id='container'>
<form id='forminsprod' class='lightgrey' action='../cgi-bin/insprod_result.cgi' method='post' enctype='multipart/form-data'>
<p id='warning'>Per inserire un nuovo prodotto, compilare il modulo sottostante.</p>";

my @ids = $radice->getElementsByTagName('id');
my $maxid = '1';
foreach $ids(@ids) {
	$idstring = $ids->string_value;
	$idcode = substr $idstring, 2;
	if($idcode > $maxid) { $maxid = $idcode; }
}
$maxid += 1;
$maxid = "ID".$maxid;

print "<ul id='ulinsprod'>
<li><input type='hidden' name='id' id='id' value='$maxid' /></li>
<li><label for='selectcateg'>Categoria: </label></td>
<select id='selectcateg' name='selectcateg' class='formmargin'>";

foreach $categoria(@categoria) {
	my $listacat = $categoria->getElementsByTagName('nomecat')->string_value;
	print "<option>$listacat</option>";
}

print "</select></li>
<li><label for='nomeprod'>Nome Prodotto: </label><input tabindex='11' type='text' id='nomeprod' name='nomeprod' class='formmargin' /></li>
<li><label for='foto'>Foto: </label><input tabindex='12' type='file' id='foto' name='foto' class='formmargin' /></li>
<li>Lavorazioni disponibili:";

my $tabindex = 13;

foreach $nomelav(@nomelav) {
	my $listalav = $nomelav->string_value;
	print "<p class='checklav formmargin'><input tabindex='$tabindex' type='checkbox' id='check$listalav' name='check$listalav' value='$listalav' /><label for='check$listalav'>$listalav</label></p>";
	$tabindex += 1;
}

print "</li>
<li><p id='pdescr'><label for='descr'>Descrizione:</label></p>
<textarea tabindex='$tabindex' id='descr' name='descr' class='formmargin'></textarea></li>
</ul>";

$tabindex += 1;

print "<input tabindex='$tabindex' type='submit' value='Inserisci Prodotto' class='submit' />
</form>
</div>";

printFOOTER();
printBODY_END();
printHTML_END();