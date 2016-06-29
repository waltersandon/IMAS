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
	<div id='container' class='lightgrey paddtop'>
	<div class='aligncenter'>
	<h1 class='infoattuale'>Lavorazione scelta:</h1>
	<img class='circolare adminfoto' src='$mfoto' alt='$malt' />
	<span class='nomescelta'>$nomelav</span>
	</div>";
	
	print "<form class='white' action='../cgi-bin/assegnalav_result.cgi' method='post'>";
	
	print "<p class='warning marginleft'>La lavorazione $nomelav è disponibile per i prodotti spuntati:</p>
	<div id='divlav'>
	<input tabindex='11' type='hidden' name='hiddennomelav' id='hiddennomelav' value='$nomelav' />
	<ul id='ulmod' class='ulnopadd formmargin'>";
	
	my $tabindex = 12;
	foreach my $listaprod(@listaprod) {
		$nomelistaprod = $listaprod->string_value;
		my $idprod = $radice->findvalue("//prodotto[nomeprod = '$nomelistaprod']/id");
		if($radice->findvalue("//prodotto[nomeprod = '$nomelistaprod']/lavorazione[text() = '$nomelav']")) {
			print "<li>
			<input tabindex='$tabindex' type='checkbox' id='check$idprod' name='check$idprod' value='$nomelistaprod' checked='checked' />
			<label for='check$idprod'>$nomelistaprod</label></li>";
		}
		else {
			print "<li>
			<input tabindex='$tabindex' type='checkbox' id='check$idprod' name='check$idprod' value='$nomelistaprod' />
			<label for='check$idprod'>$nomelistaprod</label></li>";
		}
		$tabindex += 1;
	}
	
	print "</ul>
	</div>
	<p class='noblock'><input tabindex='$tabindex' type='submit' value='Conferma Assegnazioni' id='submitassegn' class='submitchoice' /></p>
	</form>
	</div>";
}
else {
	printHTML("../public_html/parts/assegnalav_content_choice.xhtml");
	foreach $lavorazione(@lavorazione) {
			my $nomelav = $lavorazione->getElementsByTagName('nomeLav')->string_value;
			print "<option>$nomelav</option>";
	}
	print "</select></p>
	<p class='noblock'><input tabindex='12' type='submit' value='Seleziona Lavorazione' class='submitchoice' /></p>
	</form>
	</div>";
}

printFOOTER();
printBODY_END();
printHTML_END();