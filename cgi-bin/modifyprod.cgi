#!perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

checkSession();

my $cgi = new CGI;

$fileXMLprod = $fileXMLProdotti;
$fileXMLlav = $fileXMLLavorazioni;

my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($fileXMLprod);
my $radice = $doc->getDocumentElement;
my $prodotto = $cgi->param("modificaprod");

my $parserlav = XML::LibXML->new();
my $doclav = $parserlav->parse_file($fileXMLlav);
my $radicelav = $doclav->getDocumentElement;
my @nomelav = $radicelav->getElementsByTagName('nomeLav');

#recupero i parametri

my $nnome = $cgi->param("nome");
my $nfoto = $cgi->param("foto");
my $nalt = $cgi->param("alt");
my $ndescr = $cgi->param("descr");

my $error = 0;

if(!$nnome or !$nalt) { $error = 1; }

#errore lavorazioni

my $lavelemento;

my $numlav = 0;

foreach $nomelav(@nomelav) {

my $listalav = $nomelav->string_value;
if($cgi->param("check$listalav")) {
$numlav += 1;
$lavelemento .= 
"<lavorazione>$listalav</lavorazione>
";
}

}

if(!$numlav) { $error = 1; }

if(!$error) {

#modifiche semplici

my $altnodo = $radice->findnodes("//prodotto[nomeprod = '$prodotto']/alt/text()")->get_node(1);
$altnodo->setData($nalt);

#modifica descrizione

if($ndescr) {
	my $descrnodo = $radice->findnodes("//prodotto[nomeprod = '$prodotto']/descrizione/text()")->get_node(1);
	$descrnodo->setData($ndescr);
}

#modifica foto con upload e delete

if($nfoto) {
	my $imagesdir = "../public_html/images/";
	my $uploadfoto = $cgi->upload("foto");
	
	my $vecchiafoto = $radice->findvalue("//prodotto[nomeprod = '$prodotto']/foto/text()");
	unlink("$vecchiafoto") or die "Errore nella cancellazione vecchia foto!";
	
	open(UPLOADFILE,">$imagesdir/$nfoto");
	binmode UPLOADFILE;
	while(<$uploadfoto>) { print UPLOADFILE; }
	close UPLOADFILE;
	
	my $fotonodo = $radice->findnodes("//prodotto[nomeprod = '$prodotto']/foto/text()")->get_node(1);
	$fotonodo->setData($imagesdir.$nfoto);
}

#modifica lavorazioni

my @daeliminare = $radice->findnodes("//prodotto[nomeprod = '$prodotto']/lavorazione");
foreach $daeliminare (@daeliminare) {
	my $padre = $daeliminare->parentNode;
	$padre->removeChild($daeliminare);
}

my $nuovoelemento = "";

$nuovoelemento .= $lavelemento;

my $frammento = $parser->parse_balanced_chunk($nuovoelemento);
my @nodes = $doc->findnodes("//prodotto[nomeprod = '$prodotto']");
foreach my $node(@nodes) { $node->appendChild($frammento); }

#modifica nome

my $nomenodo = $radice->findnodes("//prodotto[nomeprod = '$prodotto']/nomeprod/text()")->get_node(1);
$nomenodo->setData($nnome);

open(OUT,">$fileXMLprod");
print OUT $doc->toString;
close(OUT);

}

printHTML("../public_html/parts/modprod_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/modprod_nav.xhtml");

if(!$error) {
	printHTML("../public_html/parts/modifyprod_content.xhtml");
}
else {
	printHTML("../public_html/parts/modifyprod_error.xhtml");
}

printFOOTER();
printBODY_END();
printHTML_END();