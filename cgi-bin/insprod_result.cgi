#!/usr/bin/perl

require "utility.pl";

printDOCTYPE();
printHTML_BEGIN();

checkSession();

my $cgi = new CGI;

#cattura parametri del form

my $categ = $cgi->param("selectcateg");
my $nomeprod = $cgi->param("nomeprod");
my $id = $cgi->param("id");
my $foto = $cgi->param("foto");
my $checkvern = $cgi->param("checkvern");
my $checkcrom = $cgi->param("checkcrom");
my $checktagl = $cgi->param("checktagl");
my $descr = $cgi->param("descr");

my $error = 0;

if(!$nomeprod) {
    $error = 1;
}
elsif(!$id) {
    $error = 1;
}
elsif(!$foto) {
    $error = 1;
}
elsif(!$checkvern and !$checkcrom and !$checktagl) {
    $error = 1;
}
elsif(!$descr) {
    $error = 1;
}

#nessun errore

if(!$error) {

    #elaborazione categoria

    if($categ eq gef) {	$categ = 'Griglie e fornelli'; }
    elsif($categ eq lel) { $categ = 'Laminati e lastre'; }

    #elaborazione foto

    my $imagesdir = "../public_html/images";
    my $uploadfoto = $cgi->upload("foto");

    open(UPLOADFILE,">$imagesdir/$foto");
    binmode UPLOADFILE;
    while(<$uploadfoto>) { print UPLOADFILE; }
    close UPLOADFILE;

    #inserimento nuovo prodotto

    my $xml="../data/xml/prodotti.xml";
    my $parser = XML::LibXML->new();
    my $doc = $parser->parse_file($xml) || die("Operazione di parsificazione fallita");
    my $radice = $doc->getDocumentElement || die("Non accedo alla radice");

    my $nuovoelemento =
        "<prodotto>
        <id>$id</id>
        <nomeprod>$nomeprod</nomeprod>
        <foto>$imagesdir/$foto</foto>
        <alt>Foto $nomeprod</alt>
        <descrizione>$descr</descrizione>
        ";

    if($checkvern) { $nuovoelemento .=
        "<lavorazione>Verniciatura</lavorazione>
        "; }
    if($checkcrom) { $nuovoelemento .=
        "<lavorazione>Cromatura</lavorazione>
        "; }
    if($checktagl) { $nuovoelemento .=
        "<lavorazione>Taglio</lavorazione>
        "; }

    $nuovoelemento .=
        "</prodotto>

        ";

    my $frammento = $parser->parse_balanced_chunk($nuovoelemento);
    my @nodes = $doc->findnodes("/catalogo/categoria[nomecat='$categ']");

    # print the text in the title elements
    foreach my $node (@nodes) {
        $node->appendChild($frammento);
    }

    open(OUT,">$xml");
    print OUT $doc->toString;
    close(OUT);

}

printHTML("../public_html/parts/insprod_header.xhtml");
printBODY_BEGIN();
printHEADER();

printHTML("../public_html/parts/insprod_nav.xhtml");

if(!$error) {
    printHTML("../public_html/parts/insprod_result_content.xhtml");
}
else {
    printHTML("../public_html/parts/insprod_result_content_error.xhtml");
}

printFOOTER();
printBODY_END();
printHTML_END();