#!perl
#!/usr/bin/perl

require "utility.pl";

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
my $nomeprod = $cgi->param("selectprod");

printDOCTYPE();
printHTML_BEGIN();

checkSession();

printHTML("../public_html/parts/modprod_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/modprod_nav.xhtml");

if($nomeprod and $nomeprod ne "--------") {
	my $mfoto = $radice->findvalue("//prodotto[nomeprod = '$nomeprod']/foto");
	my $malt = $radice->findvalue("//prodotto[nomeprod = '$nomeprod']/alt");
	my $mcategoria = $radice->findvalue("//prodotto[nomeprod = '$nomeprod']/../nomecat");
	my $mdescr = $radice->findvalue("//prodotto[nomeprod = '$nomeprod']/descrizione");
	printHTML("../public_html/parts/modprod_content_afterchoice.xhtml");
	print "<img class='circolare fotoprod' src='$mfoto' alt='$malt' />
	<h3>$nomeprod</h3>
	</div>";
	
	print "<form id='formmodprod' class='white' action='../cgi-bin/modifyprod.cgi' method='post' enctype='multipart/form-data' autocomplete='off'>";
	
	print "<ul id='ulmodify'>
	<li>
	<table class='tablemodify'>
	<tbody>
	<tr><td><input type='hidden' name='modificaprod' id='modificaprod' value='$nomeprod' /></td></tr>
	<tr>
	<td><label for='nome' class='textbold'>Nome: </label></td>
	<td><input type='text' name='nome' id='nome' value='$nomeprod' /></td>
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

	
	<div id='divlav'><span class='textbold'>Lavorazioni:</span>
	<ul id='ullav'>";
	
	foreach $nomelav(@nomelav) {
		my $listalav = $nomelav->string_value;
		if($radice->findvalue("//prodotto[nomeprod = '$nomeprod']/lavorazione[text()='$listalav']")) {
		print "<li class='checklav'>
		<input type='checkbox' id='check$listalav' name='check$listalav' value='$listalav' checked />
		<label for='check$listalav'>$listalav</label></li>";
		}
		else {
		print "<li class='checklav'>
		<input type='checkbox' id='check$listalav' name='check$listalav' value='$listalav' />
		<label for='check$listalav'>$listalav</label></li>";
		}
	}

	print "</ul>
	</div>
	
	<table class='tablemodify'>
	<tbody>
	<tr>
	<td><label for='descr' id='labeldescr' class='textbold'>Descrizione:</label></td>
	<td><span id='attualelabel'>Attuale:<span></td
	</tr>
	<tr>
	<td><textarea name='descr' id='descr'></textarea></td>
	<td id='attualedescr'><p>$mdescr</p></td>
	</tr>
	<tr>
	<td><input type='submit' value='Conferma Modifiche' id='confmodprod' /></td>
	</tr>
	</tbody>
	</table>
	</li>
	</ul>
	</form>";
	
	print "<form id='formdelprod' class='lightgrey' action='../cgi-bin/deleteprod.cgi' method='post'>
	<span id='testodelete'>Eliminazione prodotto:</span>
	<input type='hidden' name='eliminaprod' id='eliminaprod' value='$nomeprod' /></td></tr>
	<input type='submit' value='Elimina Prodotto' id='confdeleteprod' />
	</form>
	</div>";
}
else {
	printHTML("../public_html/parts/modprod_content_beforechoice.xhtml");
	foreach $categoria(@categoria) {
		my $listacat = $categoria->getElementsByTagName('nomecat')->string_value;
		print "<option disabled>Categoria: $listacat</option>";
		my @prodotto = $categoria->getElementsByTagName('prodotto');
		foreach $prodotto(@prodotto) {
			my $nomeprod = $prodotto->getElementsByTagName('nomeprod')->string_value;
			print "<option>$nomeprod</option>";
		}
	}
	print "</select>
	<input type='submit' value='Seleziona Prodotto' id='sceltamodprod' class='sceltaprod' />
	</div>
	</form>
	</div>";
}

printFOOTER();
printBODY_END();
printHTML_END();
