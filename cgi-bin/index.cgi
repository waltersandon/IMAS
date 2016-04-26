#!/usr/bin/perl

require "util.pl";

printDOCTYPE();
printHTML_BEGIN();
printHTML("../public_html/parts/index_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/index_nav.xhtml");


printFOOTER();
printBODY_END();
printHTML_END();
