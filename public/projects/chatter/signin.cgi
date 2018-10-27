#!/usr/bin/perl -wT
use strict; 
use CGI; 
use CGI::Carp qw ( fatalsToBrowser ); 
use File::Basename; 
$CGI::POST_MAX = 1024 * 5000;

#-------------
my $query = new CGI; 
print $query->header ( );

my $username=$query->param("username");
my $password=$query->param("password");
 
my $userExists="false";
checkNameAndPass();
printHeader();
my $strTrue="true";
if ($userExists eq $strTrue){

	#the person has an account-----------
	print qq(<h2>hi $username</h2> );
	print qq(<form action="post.cgi" method="POST">
	<input type="hidden" name="username" value="$username">
<textarea type="text" name="postText" size="160" maxlength="160" cols="28" rows="3" autofocus  required>
what do you have in mind?</textarea><br />
<button width="100" id="4" type="submit" style="padding-top:-20px;height:40px;font-size:1em;margin-left:-2px;">post!</button><br>); 
	
	#print user's recent posts:
	open(my $chatters, '<:encoding(UTF-8)', "users/$username") or die "file not opened!";
	print qq(<h4>your recent posts:</h4> );
	while (my $row = <$chatters>) {
		print qq(<pre style="text-align:left;width:280px;word-wrap: break-word;">);
		print "-$row</pre>";
		
	}
	
	print qq(<h4>today's public posts:</h4> );
	#print lines from chatters file
	open(my $chatters, '<:encoding(UTF-8)', "chatters") or die "file not opened!";
	my $count=1;
	
	while (my $row = <$chatters>) {
		print qq(<pre style="text-align:left;width:280px;word-wrap: break-word;">);
		print "-$row</pre>";
		#print "$count". "-$row</pre>";
		$count++;
	}
	
	
}
else{
	#the person does not have a account---------------
	
	print qq(<img src=stop.jpg /> );
	print qq(<p>hey, the username and password dont match!</p> );
	print qq(<p>you can try signing again <a href="signin.html">here.</a></p> );
	print qq(<p>or create an account <a href="signup.html">here.</a></p> );
}



#check if username already exists
sub checkNameAndPass
{
	my $filename = 'users.txt';
	open(my $fh, '<:encoding(UTF-8)', $filename) or die "file not opened!";
	while (my $row = <$fh>) {
		chomp $row;
		my @line=split(/:/, $row);
		if (($line[0] eq $username) && ($line[1] eq $password)){
			$userExists="true";
			#print "match found!";
		}
	}
}

sub printHeader{
	print qq(<!DOCTYPE html>
<html><head>
<link href='http://fonts.googleapis.com/css?family=Pirata+One' rel='stylesheet' type='text/css'>
<link rel="stylesheet" type="text/css" href="style.css" media="screen" />
<title>.: chatter :.</title>
<!-- script type="text/javascript">   
function refresh() 
{  
	location.reload();
} 
setTimeout('refresh()', 5000);   
</script -->

</head>
<body>
<h1><a href="http://www2.scs.ryerson.ca/~sdhayala/cgi-bin/project/">chatter!</a></h1>);
}