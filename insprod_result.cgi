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

my $parserlav = XML::LibXML->new();
my $doclav = $parserlav->parse_file($fileXMLlav);
my $radicelav = $doclav->getDocumentElement;
my @nomelav = $radicelav->getElementsByTagName('nomeLav');

#cattura parametri del form

my $categ = $cgi->param("selectcateg");
my $nomeprod = $cgi->param("nomeprod");
my $id = $cgi->param("id");
my $foto = $cgi->param("foto");
my $alt = $cgi->param("alt");
my $descr = $cgi->param("texta2");

#controllo errori

my $error = 0;

if(!$nomeprod) { $error = 1; }
elsif(!$id) { $error = 1; }
elsif(!$foto) { $error = 1; }
elsif(!$alt) { $error = 1; }
elsif(!$descr) { $error = 1; }

#errore lavorazioni

my $lavelemento;

my $numlav = 0;

foreach $nomelav(@nomelav) {

my $listalav = $nomelav->string_value;
if($cgi->param("check$listalav")) {
$numlav += 1;
$lavelemento .= 
"<lavorazione>$listalav</lavorazione>
";
}

}

if(!$numlav) { $error = 1; }

#nessun errore

if(!$error) {

#elaborazione foto

my $imagesdir = "../public_html/images";
my $uploadfoto = $cgi->upload("foto");

open(UPLOADFILE,">$imagesdir/$foto");
binmode UPLOADFILE;
while(<$uploadfoto>) { print UPLOADFILE; }
close UPLOADFILE;

#inserimento nuovo prodotto

my $nuovoelemento = "<prodotto>
<id>$id</id>
<nomeprod>$nomeprod</nomeprod>
<foto>$imagesdir/$foto</foto>
<alt>$alt</alt>
<descrizione>$descr</descrizione>
";

$nuovoelemento .= $lavelemento;

$nuovoelemento .= "</prodotto>

";

my $frammento = $parser->parse_balanced_chunk($nuovoelemento);
my @nodes = $doc->findnodes("/catalogo/categoria[nomecat='$categ']");

# print the text in the title elements
foreach my $node (@nodes) {
  $node->appendChild($frammento);
}

open(OUT,">$fileXMLprod");
print OUT $doc->toString;
close(OUT);

}

printHTML("../public_html/parts/insprod_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/insprod_nav.xhtml");

if(!$error) {
	printHTML("../public_html/parts/insprod_result_content.xhtml");
}
else {
	printHTML("../public_html/parts/insprod_result_content_error.xhtml");
}

printFOOTER();
printBODY_END();
printHTML_END();
