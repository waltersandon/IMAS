#!perl
#!/usr/bin/perl

use XML::LibXML;
use CGI;
use CGI::Session;
require "utility.pl";

read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
    ($name, $value) = split(/=/, $pair);
    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    $input{$name} = $value;
}

my $file = '../data/xml/login.xml';
#creazione oggetto parser
my $parser = XML::LibXML->new();
#apertura file e lettura input
my $doc = $parser->parse_file($file);
#estrazione elemento radice
my $radice= $doc->getDocumentElement;
my @utente = $radice->getElementsByTagName('utente');

my $inpuser = $input{'user'};
my $inppass = $input{'pass'};

my $matched = 0;

foreach $utente(@utente) {
	my $user = $utente->getElementsByTagName('username')->string_value;
	my $pass = $utente->getElementsByTagName('password')->string_value;
	if($user eq $inpuser && $pass eq $inppass) {
		$matched = 1;
		createSession();
	}
}

if($matched == 1) {
	print "<meta http-equiv='refresh' content='0;URL=insprod.cgi'>";
}
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