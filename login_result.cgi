#!/usr/bin/perl

require "utility.pl";

my $cgi = new CGI;

$inpuser = $cgi->param("user");
$inppass = $cgi->param("pass");

my $file = '../data/xml/login.xml';
#creazione oggetto parser
my $parser = XML::LibXML->new();
#apertura file e lettura input
my $doc = $parser->parse_file($file);
#estrazione elemento radice
my $radice= $doc->getDocumentElement;
my @utente = $radice->getElementsByTagName('utente');

my $matched = 0;

foreach $utente(@utente) {
    my $user = $utente->getElementsByTagName('username')->string_value;
    my $pass = $utente->getElementsByTagName('password')->string_value;
    if($user eq $inpuser && $pass eq $inppass) {
        $matched = 1;
        createSession();
    }
}

if($matched == 1) {	print "<meta http-equiv='refresh' content='0;URL=admin.cgi'>"; }
else {
    destroySession();
    printDOCTYPE();
    printHTML_BEGIN();
    printHTML("../public_html/parts/login_header.xhtml");
    printBODY_BEGIN();
    printHEADER();
    printHTML("../public_html/parts/login_nav.xhtml");
    printHTML("../public_html/parts/login_content.xhtml");

    printHTML("../public_html/parts/login_content_error.xhtml");

    printFOOTER();
    printBODY_END();
    printHTML_END();
}