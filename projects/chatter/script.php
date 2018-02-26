<?php
$fh=fopen("users.txt", 'a') or die("cant open file!");
$username=$_POST['username'];
$password=$_POST['password'];
echo fwrite($fh,$username . ':' . $password);
fclose($fh);
?>