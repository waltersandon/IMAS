
#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();
printHTML("../public_html/parts/lavorazioni_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/lavorazioni_nav.xhtml");

printTRANSFORM_lav();

printFOOTER();
printBODY_END();
printHTML_END();
