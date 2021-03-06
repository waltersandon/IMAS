#!/usr/bin/perl

require "utility.pl";

my $cgi = new CGI;

$fileXML = $fileXMLLavorazioni;

my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($fileXML);
my $radice= $doc->getDocumentElement;
my @lavorazione = $radice->getElementsByTagName('lavorazione');

#cattura parametri se il prodotto è già stato scelto
my $nomelav = $cgi->param("select");

printDOCTYPE();
printHTML_BEGIN();

checkSession();

printHTML("../public_html/parts/modlav_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/modlav_nav.xhtml");

if($nomelav and $nomelav ne "--------") {
	my $mfoto = $radice->findvalue("//lavorazione[nomeLav = '$nomelav']/fotoLav");
	my $malt = $radice->findvalue("//lavorazione[nomeLav = '$nomelav']/altLav");
	my $mproduz = $radice->findvalue("//lavorazione[nomeLav = '$nomelav']/\@produzione");
	print "<!-- Start Container -->
	<div id='container' class='lightgrey paddtop'>
	<div class='aligncenter'>
	<h1 class='infoattuale'>Stai modificando:</h1>
	<img class='circolare adminfoto' src='$mfoto' alt='$malt' />
	<span class='nomescelta'>$nomelav</span>
	</div>";
	
	print "<form class='white' action='../cgi-bin/modifylav.cgi' method='post' enctype='multipart/form-data'>";
	
	print "<p class='warning marginleft'>Per modificare una lavorazione, compilare i campi dati sottostanti:</p>
	<ul id='ulmod'>
	<li>
	<table class='tablemod'>
	<tbody>
	<tr><td><input type='hidden' name='modificalav' id='modificalav' value='$nomelav' /></td></tr>
	<tr>
	<td><label for='nome' class='textbold'>Nome: </label></td>
	<td><input tabindex='11' type='text' name='nome' id='nome' value='$nomelav' /></td>
	</tr>
	<tr>
	<td><label for='produz' class='textbold'>Produzione: </label></td>
	<td><input tabindex='12' type='text' name='produz' id='produz' value='$mproduz' /></td>
	</tr>
	<tr>
	<td><label for='foto' class='textbold'>Foto: </label></td>
	<td><input tabindex='13' type='file' name='foto' id='foto' /></td>
	</tr>
	<tr>
	<td><label for='alt' class='textbold'>Alt: </label></td>
	<td><input tabindex='14' type='text' name='alt' id='alt' value='$malt' /></td>
	</tr>
	</tbody>
	</table>
	</li>
	<li>
	<table class='tablemod'>
	<tbody>
	<tr><td><label for='texta1' id='labeldescrlav' class='textbold labeltextlav'>Descrizione:</label></td></tr>
	<tr><td><textarea tabindex='15' name='texta1' id='texta1' class='textlav' rows='0' cols='0'></textarea></td></tr>
	<tr><td><label for='texta2' id='labelcomm' class='textbold labeltextlav'>Commento:</label></td></tr>
	<tr><td><textarea tabindex='16' name='texta2' id='texta2' class='textlav' rows='0' cols='0'></textarea></td></tr>
	<tr><td><input tabindex='17' type='submit' value='Conferma Modifiche' class='submitchoice' /></td></tr>
	</tbody>
	</table>
	</li>
	</ul>
	</form>";
	
	print "<form class='lightgrey' action='../cgi-bin/deletelav.cgi' method='post'>
	<p id='testodelete' class='textbold noblock'>Eliminazione lavorazione:</p>
	<p class='noblock'><input type='hidden' name='eliminalav' id='eliminalav' value='$nomelav' /></p>
	<p class='noblock'><input tabindex='18' type='submit' value='Elimina Lavorazione' class='submitchoice redhover' /></p>
	</form>
	</div>";

}
else {
	printHTML("../public_html/parts/modlav_content_choice.xhtml");
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
