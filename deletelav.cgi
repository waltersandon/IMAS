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

my $lavorazione = $cgi->param("eliminalav");

#tolgo i nodi lavorazione da prodotti.xml

my @daeliminare = $radice->findnodes("//lavorazione[text() = '$lavorazione']");

foreach my $daeliminare(@daeliminare) {
	my $padre = $daeliminare->parentNode;
	$padre->removeChild($daeliminare);
}

open(OUT,">$fileXMLprod");
print OUT $doc->toString;
close(OUT);

#elimino la lavorazione da lavorazioni.xml

my $vecchiafoto = $radicelav->findvalue("//lavorazione[nomeLav = '$lavorazione']/fotoLav/text()");
unlink("$vecchiafoto") or die "Errore nella cancellazione vecchia foto!";

my $daeliminarelav = $radicelav->findnodes("//lavorazione[nomeLav = '$lavorazione']")->get_node(1);
my $padrelav = $daeliminarelav->parentNode;
$padrelav->removeChild($daeliminarelav);

open(OUT,">$fileXMLlav");
print OUT $doclav->toString;
close(OUT);

printHTML("../public_html/parts/modlav_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/modlav_nav.xhtml");

printHTML("../public_html/parts/deletelav_content.xhtml");

printFOOTER();
printBODY_END();
printHTML_END();
