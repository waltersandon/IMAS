#!/usr/bin/perl

require "utility.pl";

$fileXML = $fileXMLProdotti;
$fileXSLT = '../data/xsl/prodotti.xslt';

printDOCTYPE();
printHTML_BEGIN();
printHTML("../public_html/parts/prodotti_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/prodotti_nav.xhtml");

printTRANSFORM();

printFOOTER();
printBODY_END();
printHTML_END();
