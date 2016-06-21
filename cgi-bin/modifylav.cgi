#!perl
#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

checkSession();

my $cgi = new CGI;

$fileXML = $fileXMLLavorazioni;

my $parser = XML::LibXML->new();

my $doc = $parser->parse_file($fileXML);

my $radice = $doc->getDocumentElement;

my $nomelav = $cgi->param("modificaprod");

#recupero i parametri

my $nfoto = $cgi->param("foto");
my $nalt = $cgi->param("alt");
my $ndescr = $cgi->param("descrlav");
my $ncomm = $cgi->param("comm");

if(!$nfoto and !$nalt and !$ndescr and !$ncomm) { $error = 1; }

if(!$error) {

#modifiche semplici

my $altnodo = $radice->findnodes("//lavorazione[nomelav = '$nomelav']/altlav/text()")->get_node(1);
$altnodo->setData($nalt);

#modifica descrizione e commento

if($ndescr) {
	my $descrnodo = $radice->findnodes("//lavorazione[nomelav = '$nomelav']/descrlav/text()")->get_node(1);
	$descrnodo->setData($ndescr);
}

if($ncomm) {
	my $descrcomm = $radice->findnodes("//lavorazione[nomelav = '$nomelav']/commento/text()")->get_node(1);
	$descrcomm->setData($ncomm);
}

#modifica foto con upload e delete

if($nfoto) {
	my $imagesdir = "../public_html/images/";
	my $uploadfoto = $cgi->upload("foto");
	
	my $vecchiafoto = $radice->findvalue("//lavorazione[nomelav = '$nomelav']/fotolav/text()");
	unlink("$vecchiafoto") or die "Errore nella cancellazione vecchia foto!";
	
	open(UPLOADFILE,">$imagesdir/$nfoto");
	binmode UPLOADFILE;
	while(<$uploadfoto>) { print UPLOADFILE; }
	close UPLOADFILE;
	
	my $fotonodo = $radice->findnodes("//lavorazione[nomelav = '$nomelav']/fotolav/text()")->get_node(1);
	$fotonodo->setData($imagesdir.$nfoto);
}

open(OUT,">$fileXML");
print OUT $doc->toString;
close(OUT);

}

printHTML("../public_html/parts/modlav_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/modlav_nav.xhtml");

if(!$error) {
	printHTML("../public_html/parts/modifylav_content.xhtml");
}
else {
	printHTML("../public_html/parts/modifylav_error.xhtml");
}

printFOOTER();
printBODY_END();
printHTML_END();