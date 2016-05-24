#!perl
#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

destroySession();
print "<meta http-equiv='refresh' content='0;URL=../public_html/login.html'>";