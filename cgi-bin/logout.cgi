#!perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

destroySession();
print "<meta http-equiv='refresh' content='0;URL=../cgi-bin/login.cgi'>";