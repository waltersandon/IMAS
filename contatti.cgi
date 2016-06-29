#!/usr/bin/perl

require "utility.pl";

print "Content-type: text/html\n\n";
print '<!DOCTYPE html>';
	
printHTML_BEGIN();
printHTML("../public_html/parts/contatti_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/contatti_nav.xhtml");
printHTML("../public_html/parts/contatti_content.xhtml");

printFOOTER();
printBODY_END();
printHTML_END();
