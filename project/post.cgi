#!/usr/bin/perl -w
use strict; 
use CGI; 
use CGI::Carp qw ( fatalsToBrowser ); 
use File::Basename; 
$CGI::POST_MAX = 1024 * 5000;

#-------------
my $query = new CGI; 
print $query->header ( );
my $username=$query->param("username");
my $postText=$query->param("postText");
open FILE, ">>", "users/$username" or die "file not opened";
#open(my $fh, '<:encoding(UTF-8)', "users/$username) or die "file not opened!";
print FILE "$postText\n";
close(FILE);

open FILE, ">>", "chatters" or die "file chatters not opened";
#open(my $fhchatters, '<:encoding(UTF-8)', "users/$username) or die "file not opened!";
print FILE "$username:$postText\n";
close(FILE);

print qq(<!DOCTYPE html>
<html><head>
<link href='http://fonts.googleapis.com/css?family=Pirata+One' rel='stylesheet' type='text/css'>
<link rel="stylesheet" type="text/css" href="style.css" media="screen" />
<title>.: chatter :.</title>

<script type="text/javascript">   
function Redirect() 
{  
	window.history.back();
} 

setTimeout('Redirect()', 1000);   
</script>

</head>
<body>
<h1><img src="checkmark.png" width="50%" height="50%"><br />
<a href="http://www2.scs.ryerson.ca/~sdhayala/cgi-bin/project/signin.cgi">posted!</a></h1>
<br />);