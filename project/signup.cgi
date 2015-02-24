#!/usr/bin/perl -w
use strict; 
use CGI; 
use CGI::Carp qw ( fatalsToBrowser ); 
use File::Basename; 
$CGI::POST_MAX = 1024 * 5000;
#-------------
my $query = new CGI; 
my $username=$query->param("username");
my $password=$query->param("password");


my $userExists="false";
open DATA, ">>users.txt";

print $query->header ( ); #idk why this exists but its vital

checkName();
printHeader();
my $strF="false"; #couldnt compare str to false
if ($userExists eq $strF){
	print DATA $username . ":" . $password . "\n";
	#print qq(<!DOCTYPE html><p>successful</p></html>);
	#my $userFile=$username . ".txt";
	open FILE, ">", "users/$username" or die "file not opened";
	#open(my $fhand, '<:encoding(UTF-8)', $username) or die "file not opened!";
	#print FILE "acc created";
	close FILE;
	userCreated();
}
else{
	userAlreadyExists();
}
close DATA;

#check if username already exists
sub checkName
{
	my $userList = 'users.txt';
	open(my $fh, '<:encoding(UTF-8)', $userList) or die "file not opened!";
	while (my $row = <$fh>) {
		chomp $row;
		my @line=split(/:/, $row);
		if ($line[0] eq $username){
			$userExists="true";
			#print "match found!";
		}
		#print "$row\n is $line[0] and $line[1] end";
		#print "\n";
	}
}

sub printHeader{
	print qq(<!DOCTYPE html>
<html><head>
<link href='http://fonts.googleapis.com/css?family=Pirata+One' rel='stylesheet' type='text/css'>
<link rel="stylesheet" type="text/css" href="style.css" media="screen" />
<title>.: chatter :.</title></head>
<body>
<h1><a href="http://www2.scs.ryerson.ca/~sdhayala/cgi-bin/project/">chatter!</a></h1>
<br />);
}

sub userAlreadyExists{
	print qq(<p>the username already exists. <br><a href="signup.html">try a different username.</a></p>);
}

sub userCreated
{
	print qq(<p>your account has been created. <br>you just have to <a href="signin.html">sign in!</a></p>);
}