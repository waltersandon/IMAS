
#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();
printHTML("../public_html/parts/contatti_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/contatti_nav.xhtml");
printHTML("../public_html/parts/contatti_content.xhtml");

printFOOTER();
printBODY_END();
printHTML_END();
