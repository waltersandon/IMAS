#!/usr/bin/perl

require "utility.pl";

my $cgi = new CGI;

$fileXML = $fileXMLProdotti;

my $parser = XML::LibXML->new();

my $doc = $parser->parse_file($fileXML);

my $radice = $doc->getDocumentElement;

my $prodotto = $cgi->param("eliminaprod");

my $daeliminare = $radice->findnodes("//prodotto[nomeprod = '$prodotto']")->get_node(1);

my $padre = $daeliminare->parentNode;

$padre->removeChild($daeliminare);

open(OUT,">$fileXML");
print OUT $doc->toString;
close(OUT);

printDOCTYPE();
printHTML_BEGIN();

checkSession();

printHTML("../public_html/parts/modprod_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/modprod_nav.xhtml");
printHTML("../public_html/parts/deleteprod_content.xhtml");

printFOOTER();
printBODY_END();
printHTML_END();
