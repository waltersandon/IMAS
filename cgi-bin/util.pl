use XML::LibXSLT;
use XML::LibXML;


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

sub stampa {
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