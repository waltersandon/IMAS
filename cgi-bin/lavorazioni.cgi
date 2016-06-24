#!/usr/bin/perl

require "utility.pl";

$fileXML = $fileXMLLavorazioni;
$fileXSLT = '../data/xsl/lavorazioni.xslt';

printDOCTYPE();
printHTML_BEGIN();
printHTML("../public_html/parts/lavorazioni_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/lavorazioni_nav.xhtml");

printTRANSFORM();

printFOOTER();
printBODY_END();
printHTML_END();
