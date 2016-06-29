#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

checkSession();

printHTML("../public_html/parts/inslav_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/inslav_nav.xhtml");

printHTML("../public_html/parts/inslav_content.xhtml");

printFOOTER();
printBODY_END();
printHTML_END();