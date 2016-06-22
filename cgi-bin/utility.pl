use XML::LibXML;
use XML::LibXSLT;
use CGI;
use CGI::Session;

$fileXMLProdotti = '../data/xml/prodotti.xml';
$fileXMLLavorazioni = '../data/xml/lavorazioni.xml';

sub printHTML {
    open (FILE, $_[0]) || die "Cannot open '$_[0]': $!";
    print join '', <FILE>;
}

sub printDOCTYPE {
    print "Content-type: text/html\n\n";
    print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">';
}

sub printHTML_BEGIN {
    print '<html xml:lang="it" lang="it" xmlns="http://www.w3.org/1999/xhtml">';
}

sub printHTML_END {
    print '</html>';
}

sub printBODY_BEGIN {
    print '<body>';
}

sub printBODY_END {
    print '</body>';
}

sub printHEADER {
	$session = CGI::Session->load() or die $!;
	if(($session->is_expired || $session->is_empty )) { printHTML("../public_html/parts/header.xhtml"); }
	else {
	$utente = $session->param('username');
	print '<div id="header">
	<img id="logoDitta" src="../public_html/images/logoimas.png" alt="Logo Imas">
	</div>
	<div id="adminzone"> 
	<p><span id="benvenuto">';
	print "Buongiorno, $utente.";
	print '</span><span id="scelteadmin"><a id="logout" href="../cgi-bin/admin.cgi" tabindex="1">Amministrazione</a> | <a id="logout" href="../cgi-bin/logout.cgi" tabindex="2">Logout</a><span></p>
    </div>
	<div id="panoramicphoto">
	 <img id="panoramic" src="../public_html/images/panoramic.jpg" alt="Foto Panoramica" />
	</div>';
	}
}

sub printFOOTER {
    printHTML("../public_html/parts/footer.xhtml");
}

sub printTRANSFORM_prodotti {
    my $xslt = XML::LibXSLT->new();
    
    my $source = XML::LibXML->load_xml(location =>"$fileXML");
    my $style_doc = XML::LibXML->load_xml(location=>"$fileXSLT", no_cdata=>1);
    
    my $stylesheet = $xslt->parse_stylesheet($style_doc);
    
    my $results = $stylesheet->transform($source);
    
    print $stylesheet->output_string($results);
}

sub printTRANSFORM_lav {
    my $xslt = XML::LibXSLT->new();
    
    my $source = XML::LibXML->load_xml(location =>"$fileXMLLavorazioni");
    my $style_doc = XML::LibXML->load_xml(location=>"$fileXSLTLavorazioni", no_cdata=>1);
    
    my $stylesheet = $xslt->parse_stylesheet($style_doc);
    
    my $results = $stylesheet->transform($source);
    
    print $stylesheet->output_string($results);
}

sub createSession() {
    $session = CGI::Session->new();
    $session->param('username',"$inpuser");
	$session->param('password',"$inppass");
    print $session->header();
}

sub getSession() {
    $session = CGI::Session->load() or die $!;
    if ($session->is_expired || $session->is_empty ) {
        return false;
    } else {
        my $utente = $session->param('username');
        return true;
    }
}

sub destroySession() {
    $session = CGI::Session->load() or die $!;
    $session->close();
    $session->delete();
    $session->flush();
}

sub checkSession() {
	if(getSession() eq false) {
		print "<meta http-equiv='refresh' content='0;URL=../cgi-bin/login.cgi'>";
	}
}