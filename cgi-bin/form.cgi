#!perl

use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $q = new CGI;

print $q->header;

print $q->start_html(-title => 'A web form');