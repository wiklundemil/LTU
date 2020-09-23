<link rel="stylesheet" type="text/css" href="style.css">

<?php
	session_start();
		
	if(!isset($_SESSION['inloggad'])){
		
		include'hariskod_login.php';
		
	}
	else{

	}

	if(isset($_SESSION['inloggad'])){
		
		header('Location:Start.php');

	}
	else{

	}
	//Förklaras i martinskod.php.
?>
