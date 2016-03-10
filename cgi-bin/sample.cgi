#!perl

use CGI qw(:standard);
use Net::SMTP;

$smtp = Net::SMTP->new("smtp.libero.it ");

print <<END;
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
END

$regfile = 'registrations.txt';

$name = param('name');
$email = param('email');
$food = param('food');



$smtp->mail("kutinju@libero.it");
$smtp->to($email);
$smtp->data();
$smtp->datasend("Ciao!");
$smtp->dataend();
$smtp->quit;

open(REG,">>$regfile") or fail();
print REG "$name\t$email\t$food\n";
close(REG);

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) =
    gmtime(time);
$now = sprintf "%4d-%02d-%02dT%02d:%02dZ\n",
    1900+$year,$mon+1,$mday,$hour,$min;

print <<END;
<title>Thank you!</title>
<h1>Thank you!</h1>
<p>Your fake registration to Virtual Nonsense Party
has been recorded at $now as follows:</p>
<p>Name: $name</p>
<p>E-mail: $email</p>
<p>Food preference: $food</p>
END

sub fail {
   print "<title>Error</title>",
   "<p>Error: cannot record your registration!</p>";
   exit; }