#!perl

require "util.pl";

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