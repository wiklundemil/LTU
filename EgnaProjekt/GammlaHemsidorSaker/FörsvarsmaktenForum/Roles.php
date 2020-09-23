<link rel="stylesheet" type="text/css" href="style.css">
<?php

	include 'config.php';
	include 'Send.php';


	$HeadAdmin = 3;
	$Admin = 2;
	$Moderator = 1;
	$User = 0;

	$stmt = $dbh->prepare('SELECT roles FROM account');
	$result = $stmt->execute();
	
	if($_SESSION['role'] == $HeadAdmin){

		include'table_info.php';		

	}
	else{

	}
	?>

