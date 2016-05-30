#!perl
#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

if(getSession() eq false) {
	print "<meta http-equiv='refresh' content='0;URL=../public_html/login.html'>";
}

printHTML("../public_html/parts/prodotti_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/prodotti_nav.xhtml");

printFOOTER();
printBODY_END();
printHTML_END();