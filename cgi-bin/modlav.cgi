#!perl

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
	<div id='container' class='lightgrey result'>
	<h3 class='infoattuale'>Stai modificando: </h3>
	<img class='circolare fotoprod' src='$mfoto' alt='$malt' />
	<h3>$nomelav</h3>";
	
	print "<form class='white' action='../cgi-bin/modifylav.cgi' method='post' enctype='multipart/form-data' autocomplete='off'>";
	
	print "<ul id='ulmod'>
	<li>
	<table class='tablemod'>
	<tbody>
	<tr><td><input type='hidden' name='modificalav' id='modificalav' value='$nomelav' /></td></tr>
	<tr>
	<td><label for='nome' class='textbold'>Nome: </label></td>
	<td><input type='text' name='nome' id='nome' value='$nomelav' /></td>
	</tr>
	<tr>
	<td><label for='produz' class='textbold'>Produzione: </label></td>
	<td><input type='text' name='produz' id='produz' value='$mproduz' /></td>
	</tr>
	<tr>
	<td><label for='foto' class='textbold'>Foto: </label></td>
	<td><input type='file' name='foto' id='foto' /></td>
	</tr>
	<tr>
	<td><label for='alt' class='textbold'>Alt: </label></td>
	<td><input type='text' name='alt' id='alt' value='$malt' /></td>
	</tr>
	</tbody>
	</table>
	</li>
	
	<table class='tablemod'>
	<tbody>
	<tr><td><label for='descrlav' id='labeldescrlav' class='textbold labeltextlav'>Descrizione:</label></td></tr>
	<tr><td><textarea name='descrlav' id='descrlav' class='textlav'></textarea></td></tr>
	<tr><td><label for='comm' id='labelcomm' class='textbold labeltextlav'>Commento:</label></td></tr>
	<tr><td><textarea name='comm' id='comm' class='textlav'></textarea></td></tr>
	<tr><td><input type='submit' value='Conferma Modifiche' class='submitchoice' /></td></tr>
	</tbody>
	</table>
	</li>
	</ul>
	</form>";
	
	print "<form id='formdelprod' class='lightgrey' action='../cgi-bin/deletelav.cgi' method='post'>
	<span id='testodelete' class='textbold'>Eliminazione lavorazione:</span>
	<input type='hidden' name='eliminalav' id='eliminalav' value='$nomelav' /></td></tr>
	<input type='submit' value='Elimina Lavorazione' id='confdeleteprod' class='submitchoice redhover' />
	</form>
	</div>";

}
else {
	printHTML("../public_html/parts/modlav_content_choice.xhtml");
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
