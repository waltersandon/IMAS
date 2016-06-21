#!perl
#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

checkSession();

my $cgi = new CGI;

$fileXML = $fileXMLProdotti;

my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($fileXML);
my $radice = $doc->getDocumentElement;
my @categoria = $radice->getElementsByTagName('categoria');

printHTML("../public_html/parts/insprod_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/insprod_nav.xhtml");

print "<!-- Start Container -->
<div id='container'>
<form id='forminsprod' class='lightgrey' action='../cgi-bin/insprod_result.cgi' method='post' enctype='multipart/form-data'>
<p id='warning'>Per inserire un nuovo prodotto, compilare il modulo sottostante.</p>
<ul id='ulinsprod'>
<li><label for='selectcateg'>Categoria: </label></td>
<select id='selectcateg' name='selectcateg' class='formmargin'>";

foreach $categoria(@categoria) {
	my $listacat = $categoria->getElementsByTagName('nomecat')->string_value;
	print "<option>$listacat</option>";
}

printHTML("../public_html/parts/insprod_content.xhtml");

printFOOTER();
printBODY_END();
printHTML_END();