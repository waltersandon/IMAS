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
my $nomelav = $cgi->param("selectprod");

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
	<div id='container' class='lightgrey containerbottom'>
	<div id='divmodprod'>
	<h3 id='titoloprod'>Lavorazione scelta: </h3>
	<img class='circolare fotoprod' src='$mfoto' alt='$malt' />
	<h3>$nomelav</h3>
	</div>";
	
	print "<form id='formmodprod' class='white' action='../cgi-bin/assegnalav_result.cgi' method='post' autocomplete='off'>";
	
	print "<div id='divlav'>
	<h2>Elenco prodotti: </h2>
	<p>La $nomelav è disponibile per i prodotti spuntati:</p>
	<input type='hidden' name='hiddennomelav' id='hiddennomelav' value='$nomelav' />
	<ul id='ulmodify'>";
	
	foreach my $listaprod(@listaprod) {
		$nomelistaprod = $listaprod->string_value;
		if($radice->findvalue("//prodotto[nomeprod = '$nomelistaprod']/lavorazione[text() = '$nomelav']")) {
			print "<li class='checklav'>
			<input type='checkbox' id='check$nomelistaprod' name='check$nomelistaprod' value='$nomelistaprod' checked />
			<label for='check$nomelistaprod'>$nomelistaprod</label></li>";
		}
		else {
			print "<li class='checklav'>
			<input type='checkbox' id='check$nomelistaprod' name='check$nomelistaprod' value='$nomelistaprod' />
			<label for='check$nomelistaprod'>$nomelistaprod</label></li>";
		}
	}
	
	print "</ul>
	<input type='submit' value='Conferma Assegnazioni' id='confmodprod' />
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
	<input type='submit' value='Seleziona Lavorazione' id='sceltamodprod' class='sceltaprod' />
	</form>
	</div>";
}

printFOOTER();
printBODY_END();
printHTML_END();
