#!perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

checkSession();

printHTML("../public_html/parts/admin_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/admin_nav.xhtml");
printHTML("../public_html/parts/admin_content.xhtml");

printFOOTER();
printBODY_END();
printHTML_END();