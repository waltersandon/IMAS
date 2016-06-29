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
my @categoria = $radice->getElementsByTagName('categoria');

my $parserlav = XML::LibXML->new();
my $doclav = $parserlav->parse_file($fileXMLlav);
my $radicelav = $doclav->getDocumentElement;
my @nomelav = $radicelav->getElementsByTagName('nomeLav');

#cattura parametri se il prodotto è già stato scelto
my $nomeprod = $cgi->param("select");

printHTML("../public_html/parts/modprod_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/modprod_nav.xhtml");

if($nomeprod and $nomeprod ne "--------") {
	my $mfoto = $radice->findvalue("//prodotto[nomeprod = '$nomeprod']/foto");
	my $malt = $radice->findvalue("//prodotto[nomeprod = '$nomeprod']/alt");
	my $mcategoria = $radice->findvalue("//prodotto[nomeprod = '$nomeprod']/../nomecat");
	my $mdescr = $radice->findvalue("//prodotto[nomeprod = '$nomeprod']/descrizione");
	print "<!-- Start Container -->
	<div id='container' class='lightgrey paddtop'>
	<div class='aligncenter'>
	<h1 class='infoattuale'>Stai modificando:</h1>
	<img class='circolare adminfoto' src='$mfoto' alt='$malt' />
	<span class='nomescelta'>$nomeprod</span>
	</div>";

	print "<form class='white' action='../cgi-bin/modifyprod.cgi' method='post' enctype='multipart/form-data'>";
	
	print "<p class='warning marginleft'>Per modificare un prodotto, compilare i campi dati sottostanti:</p>
	<ul id='ulmod'>
	<li>
	<table class='tablemod'>
	<tbody>
	<tr><td><input type='hidden' name='modificaprod' id='modificaprod' value='$nomeprod' /></td></tr>
	<tr>
	<td><label for='nome' class='textbold'>Nome: </label></td>
	<td><input tabindex='12' type='text' name='nome' id='nome' value='$nomeprod' /></td>
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
	<table class='tablemod'>
	<tbody>
	<tr><td>
	<span class='textbold'>Lavorazioni disponibili:</span>";
	
	my $tabindex = 15;
	foreach $nomelav(@nomelav) {
		my $listalav = $nomelav->string_value;
		if($radice->findvalue("//prodotto[nomeprod = '$nomeprod']/lavorazione[text() = '$listalav']")) {
		print "<p class='standardcheckb'><input tabindex='$tabindex' type='checkbox' id='check$listalav' name='check$listalav' value='$listalav' checked='checked' /><label for='check$listalav'>$listalav</label></p>";
		}
		else {
		print "<p class='standardcheckb'><input tabindex='$tabindex' type='checkbox' id='check$listalav' name='check$listalav' value='$listalav' /><label for='check$listalav'>$listalav</label></p>";
		}
		$tabindex += 1;
	}

	print "</td></tr>
	</tbody>
	</table>
	<table class='tablemod'>
	<tbody>
	<tr>
	<td><p id='attualelabel' class='textbold'>Descrizione Attuale:</p></td>
	</tr>
	<tr>
	<td><p id='attualedescr'>$mdescr</p></td>
	</tr>
	<tr>
	<td><label for='texta2' class='textbold'>Descrizione:</label></td>
	</tr>
	<tr>
	<td><textarea tabindex='$tabindex' name='texta2' id='texta2' rows='0' cols='0'></textarea></td>
	</tr>";
	
	$tabindex += 1;
	
	print "<tr>
	<td><input tabindex='$tabindex' type='submit' value='Conferma Modifiche' class='submitchoice' /></td>
	</tr>
	</tbody>
	</table>
	</li>
	</ul>
	</form>";
	
	$tabinxed += 1;
	
	print "<form class='lightgrey' action='../cgi-bin/deleteprod.cgi' method='post'>
	<p id='testodelete' class='textbold noblock'>Eliminazione prodotto:</p>
	<p class='noblock'><input type='hidden' name='eliminaprod' id='eliminaprod' value='$nomeprod' /></p>
	<p class='noblock'><input tabindex='$tabindex' type='submit' value='Elimina Prodotto' class='submitchoice redhover' /></p>
	</form>
	</div>";
}
else {
	printHTML("../public_html/parts/modprod_content_choice.xhtml");
	foreach $categoria(@categoria) {
		my $listacat = $categoria->getElementsByTagName('nomecat')->string_value;
		print "<option disabled='disabled'>Categoria: $listacat</option>";
		my @prodotto = $categoria->getElementsByTagName('prodotto');
		foreach $prodotto(@prodotto) {
			my $nomeprod = $prodotto->getElementsByTagName('nomeprod')->string_value;
			print "<option>$nomeprod</option>";
		}
	}
	print "</select></p>
	<p class='noblock'><input tabindex='12' type='submit' value='Seleziona Prodotto' class='submitchoice' /></p>
	</form>
	</div>";
}

printFOOTER();
printBODY_END();
printHTML_END();
