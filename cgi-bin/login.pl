#!perl

use XML::LibXML;

print "Content-type:text/html\n\n";

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
my @elementi = $radice->getElementsByTagName('utenti');
my @user = $radice->getElementsByTagName('username');
my @pass = $radice->getElementsByTagName('password');

my $inpuser = $input{'user'};
my $inppass = $input{'pass'};

my $retlink = '.../public_html/home.html';

my $matched = 0;

print "<html><head><title>Login</title></head><body>";

foreach $user (@user) {
	if($inpuser eq ($user->string_value)) {
		$matched = 1;
		print "Benvenuto $inpuser!\n\n";
		print "Torna alla <a href=\"../public_html/home.html\">home</a>";
		}
}

if($matched == 0) { 
		print "Dati inseriti errati!\n\n";
		print "<a href=\"../public_html/login.html\">Riprova</a> oppure torna alla <a href=\"../public_html/home.html\">home</a>";
}

print "</body></html>";
