use XML::LibXML;
use XML::LibXSLT;
use CGI;
use CGI::Session;

my $fileXMLAdmin = '../data/xml/admin.xml';
my $fileXMLProdotti = '../data/xml/.xml';

sub connectXMLAdmin() {
    #creazione oggetto parser
    my $parser = XML::LibXML->new();
    
    #apertura file e lettura input
    return $parser->parse_file($fileXMLAdmin) || die("Operazione di parsificazione fallita");
}

sub connectXMLProdotti() {
    #creazione oggetto parser
    my $parser = XML::LibXML->new();
    
    #apertura file e lettura input
    return $parser->parse_file($fileXMLProdotti) || die("Operazione di parsificazione fallita");
}

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
    printHTML("../public_html/parts/header.xhtml");
}
sub printFOOTER {
    printHTML("../public_html/parts/footer.xhtml");
}

sub printTRANSFORM {
	my $xslt = XML::LibXSLT->new();

	my $source = XML::LibXML->load_xml(location => '../data/xml/prodotti.xml');
	my $style_doc = XML::LibXML->load_xml(location=>'../data/xsl/prodotti.xsl', no_cdata=>1);

	my $stylesheet = $xslt->parse_stylesheet($style_doc);

	my $results = $stylesheet->transform($source);

	print $stylesheet->output_as_bytes($results);
}

sub createSession() {
    $session = CGI::Session->new();
    $session->param('username',"$inpuser");
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