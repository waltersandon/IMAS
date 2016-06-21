#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

printHTML("../public_html/parts/index_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/index_nav.xhtml");
printHTML("../public_html/parts/index_content.xhtml");

printFOOTER();
printBODY_END();
printHTML_END();
