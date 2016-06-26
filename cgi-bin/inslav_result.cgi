#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

checkSession();

my $cgi = new CGI;

$fileXMLlav = $fileXMLLavorazioni;

my $parserlav = XML::LibXML->new();
my $doclav = $parserlav->parse_file($fileXMLlav);
my $radicelav = $doclav->getDocumentElement;
my @listalav = $radicelav->getElementsByTagName('nomeLav');

#cattura parametri del form

my $nomelav = $cgi->param("nomelav");
my $produz = $cgi->param("produz");
my $foto = $cgi->param("foto");
my $alt = $cgi->param("alt");
my $descr = $cgi->param("texta1");
my $comm = $cgi->param("texta2");

#controllo errori

my $error = 0;

if(!$nomelav) { $error = 1; }
elsif(!$produz) { $error = 1; }
elsif(!$foto) { $error = 1; }
elsif(!$alt) { $error = 1; }
elsif(!$descr) { $error = 1; }
elsif(!$comm) { $error = 1; }

foreach my $listalav(@listalav) {
	$listalav = $listalav->string_value;
	if($nomelav eq $listalav) { $error = 1; }
}

#nessun errore

if(!$error) {

#elaborazione foto

my $imagesdir = "../public_html/images";
my $uploadfoto = $cgi->upload("foto");

open(UPLOADFILE,">$imagesdir/$foto");
binmode UPLOADFILE;
while(<$uploadfoto>) { print UPLOADFILE; }
close UPLOADFILE;

#inserimento nuova lavorazione

my $nuovoelemento = "<lavorazione produzione='$produz'>
<nomeLav>$nomelav</nomeLav>
<fotoLav>$imagesdir/$foto</fotoLav>
<altLav>$alt</altLav>
<descrLav>
$descr
</descrLav>
<commento>
$comm
</commento>
</lavorazione>

";

my $frammento = $parserlav->parse_balanced_chunk($nuovoelemento);
my @nodes = $doclav->findnodes("/lavorazioni");

# print the text in the title elements
foreach my $node(@nodes) {
  $node->appendChild($frammento);
}

open(OUT,">$fileXMLlav");
print OUT $doclav->toString;
close(OUT);

}

printHTML("../public_html/parts/inslav_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/inslav_nav.xhtml");

if(!$error) {
	printHTML("../public_html/parts/inslav_result_content.xhtml");
}
else {
	printHTML("../public_html/parts/inslav_result_content_error.xhtml");
}

printFOOTER();
printBODY_END();
printHTML_END();