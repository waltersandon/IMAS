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

my $nnome = $cgi->param("nome");
my $nproduz = $cgi->param("produz");
my $nfoto = $cgi->param("foto");
my $nalt = $cgi->param("alt");
my $ndescr = $cgi->param("descrlav");
my $ncomm = $cgi->param("comm");

if(!$nnome and !$nproduz and !$nfoto and !$nalt and !$ndescr and !$ncomm) { $error = 1; }

if(!$error) {

#modifiche semplici

my $produznodo = $radice->findnodes("//lavorazione[nomeLav = '$nomelav']")->get_node(1);
$produznodo->setAttribute('produzione',$nproduz);

my $altnodo = $radice->findnodes("//lavorazione[nomeLav = '$nomelav']/altLav/text()")->get_node(1);
$altnodo->setData($nalt);

#modifica descrizione e commento

if($ndescr) {
	my $descrnodo = $radice->findnodes("//lavorazione[nomeLav = '$nomelav']/descrLav/text()")->get_node(1);
	$descrnodo->setData($ndescr);
}

if($ncomm) {
	my $descrcomm = $radice->findnodes("//lavorazione[nomeLav = '$nomelav']/commento/text()")->get_node(1);
	$descrcomm->setData($ncomm);
}

#modifica foto con upload e delete

if($nfoto) {
	my $imagesdir = "../public_html/images/";
	my $uploadfoto = $cgi->upload("foto");
	
	my $vecchiafoto = $radice->findvalue("//lavorazione[nomeLav = '$nomelav']/fotoLav/text()");
	unlink("$vecchiafoto") or die "Errore nella cancellazione vecchia foto!";
	
	open(UPLOADFILE,">$imagesdir/$nfoto");
	binmode UPLOADFILE;
	while(<$uploadfoto>) { print UPLOADFILE; }
	close UPLOADFILE;
	
	my $fotonodo = $radice->findnodes("//lavorazione[nomeLav = '$nomelav']/fotoLav/text()")->get_node(1);
	$fotonodo->setData($imagesdir.$nfoto);
}

#modifica nome

my $nomenodo = $radice->findnodes("//lavorazione[nomeLav = '$nomelav']/nomeLav/text()")->get_node(1);
$nomenodo->setData($nnome);

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
