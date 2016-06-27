#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

printHTML("../public_html/parts/login_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/login_nav.xhtml");
printHTML("../public_html/parts/login_content.xhtml");

printFOOTER();
printBODY_END();
printHTML_END();