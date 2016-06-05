
#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

checkSession();

printHTML("../public_html/parts/insprod_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/insprod_nav.xhtml");
printHTML("../public_html/parts/insprod_content.xhtml");

printFOOTER();
printBODY_END();
printHTML_END();