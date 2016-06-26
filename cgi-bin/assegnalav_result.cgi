#!/usr/bin/perl
#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

checkSession();

my $cgi = new CGI;

$fileXML = $fileXMLProdotti;

my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($fileXML);
my $radice = $doc->getDocumentElement;

my @prodotto = $radice->findnodes("//prodotto");

my $nomelav = $cgi->param("hiddennomelav");

printHTML("../public_html/parts/assegnalav_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/assegnalav_nav.xhtml");

foreach $prodotto(@prodotto) {
	my $nomeprod = $prodotto->getElementsByTagName('nomeprod')->string_value;
	if($cgi->param("check$nomeprod")) {
		if(!$radice->findvalue("//prodotto[nomeprod = '$nomeprod']/lavorazione[text() = '$nomelav']")) {
			my $nuovoelemento = 
"<lavorazione>$nomelav</lavorazione>
";
			my $frammento = $parser->parse_balanced_chunk($nuovoelemento);
			my $padre = $doc->findnodes("//prodotto[nomeprod = '$nomeprod']")->get_node(1);
			$padre->appendChild($frammento); 
		}
	}
	else {
		if($radice->findvalue("//prodotto[nomeprod = '$nomeprod']/lavorazione[text() = '$nomelav']")) {
			my $daeliminare = $radice->findnodes("//prodotto[nomeprod = '$nomeprod']/lavorazione[text() = '$nomelav']")->get_node(1);
			my $padre = $daeliminare->parentNode;
			$padre->removeChild($daeliminare);
		}
	}
}

open(OUT,">$fileXML");
print OUT $doc->toString;
close(OUT);

printHTML("../public_html/parts/assegnalav_result_content.xhtml");

printFOOTER();
printBODY_END();
printHTML_END();
