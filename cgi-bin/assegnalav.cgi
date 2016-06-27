#!/usr/bin/perl

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

my $parserlav = XML::LibXML->new();
my $doclav = $parserlav->parse_file($fileXMLlav);
my $radicelav = $doclav->getDocumentElement;

my @lavorazione = $radicelav->getElementsByTagName('lavorazione');

#cattura parametri se il prodotto è già stato scelto
my $nomelav = $cgi->param("select");

my @listaprod = $radice->findnodes("//prodotto/nomeprod");

printHTML("../public_html/parts/assegnalav_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/assegnalav_nav.xhtml");

if($nomelav and $nomelav ne "--------") {
	my $mfoto = $radicelav->findvalue("//lavorazione[nomeLav = '$nomelav']/fotoLav");
	my $malt = $radicelav->findvalue("//lavorazione[nomeLav = '$nomelav']/altLav");
	my $mproduz = $radicelav->findvalue("//lavorazione[nomeLav = '$nomelav']/\@produzione");
	print "<!-- Start Container -->
	<div id='container' class='lightgrey result'>
	<h3 class='infoattuale'>Lavorazione scelta: </h3>
	<img class='circolare fotoprod' src='$mfoto' alt='$malt' />
	<h3>$nomelav</h3>";
	
	print "<form class='white' action='../cgi-bin/assegnalav_result.cgi' method='post' autocomplete='off'>";
	
	print "<div class='divlav'>
	<h2>Elenco prodotti: </h2>
	<p>La $nomelav è disponibile per i prodotti spuntati:</p>
	</div>
	<input type='hidden' name='hiddennomelav' id='hiddennomelav' value='$nomelav' />
	<ul id='ulmod'>";
	
	foreach my $listaprod(@listaprod) {
		$nomelistaprod = $listaprod->string_value;
		if($radice->findvalue("//prodotto[nomeprod = '$nomelistaprod']/lavorazione[text() = '$nomelav']")) {
			print "<li>
			<input type='checkbox' id='check$nomelistaprod' name='check$nomelistaprod' value='$nomelistaprod' checked />
			<label for='check$nomelistaprod'>$nomelistaprod</label></li>";
		}
		else {
			print "<li>
			<input type='checkbox' id='check$nomelistaprod' name='check$nomelistaprod' value='$nomelistaprod' />
			<label for='check$nomelistaprod'>$nomelistaprod</label></li>";
		}
	}
	
	print "</ul>
	<input type='submit' value='Conferma Assegnazioni' class='submitchoice' />
	</div>
	</form>";
}
else {
	printHTML("../public_html/parts/assegnalav_content_choice.xhtml");
	foreach $lavorazione(@lavorazione) {
			my $nomelav = $lavorazione->getElementsByTagName('nomeLav')->string_value;
			print "<option>$nomelav</option>";
	}
	print "</select>
	<input type='submit' value='Seleziona Lavorazione' class='submitchoice' />
	</form>
	</div>";
}

printFOOTER();
printBODY_END();
printHTML_END();
