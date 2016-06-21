#!/usr/bin/perl

require "utility.pl";

my $cgi = new CGI;

$fileXML = $fileXMLLavorazioni;
$fileXSLT = '../data/xsl/modlav.xslt';

#creazione oggetto parser
my $parser = XML::LibXML->new();
#apertura file e lettura input
my $doc = $parser->parse_file($fileXML);
#estrazione elemento radice
my $radice= $doc->getDocumentElement;
my @lavorazione = $radice->getElementsByTagName('lavorazione');

#cattura parametri se il prodotto è già stato scelto
my $nomelav = $cgi->param("selectprod");

printDOCTYPE();
printHTML_BEGIN();

checkSession();

printHTML("../public_html/parts/modlav_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/modlav_nav.xhtml");

if($nomelav and $nomelav ne "--------") {
	my $mfoto = $radice->findvalue("//lavorazione[nomelav = '$nomelav']/fotolav");
	my $malt = $radice->findvalue("//lavorazione[nomelav = '$nomelav']/altlav");
	printHTML("../public_html/parts/modprod_content_afterchoice.xhtml");
	print "<img class='circolare fotoprod' src='$mfoto' alt='$malt' />
	<h3>$nomelav</h3>
	</div>";
	
	print "<form id='formmodprod' class='white' action='../cgi-bin/modifylav.cgi' method='post' enctype='multipart/form-data' autocomplete='off'>";
	
	print "<ul id='ulmodify'>
	<li>
	<table class='tablemodify'>
	<tbody>
	<tr><td><input type='hidden' name='modificaprod' id='modificaprod' value='$nomelav' /></td></tr>
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
	
	<table class='tablemodify'>
	<tbody>
	<tr><td><label for='descrlav' id='labeldescrlav' class='textbold labeltextlav'>Descrizione:</label></td></tr>
	<tr><td><textarea name='descrlav' id='descrlav' class='textlav'></textarea></td></tr>
	<tr><td><label for='comm' id='labelcomm' class='textbold labeltextlav'>Commento:</label></td></tr>
	<tr><td><textarea name='comm' id='comm' class='textlav'></textarea></td></tr>
	<tr><td><input type='submit' value='Conferma Modifiche' id='confmodprod' /></td></tr>
	</tbody>
	</table>
	</li>
	</ul>
	</form>
	</div>";

}
else {
	printHTML("../public_html/parts/modlav_content_beforechoice.xhtml");
	foreach $lavorazione(@lavorazione) {
			my $nomelav = $lavorazione->getElementsByTagName('nomelav')->string_value;
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
