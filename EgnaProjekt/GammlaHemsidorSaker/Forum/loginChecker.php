<link rel="stylesheet" type="text/css" href="style2.css">

<?php
		
	if(!isset($_SESSION['inloggad'])){
		
		include'hariskod_login.php';
		
	}
	else{

	}

	if(isset($_SESSION['inloggad'])){
		
		include'Logout.php';

	}
	else{

	}
	//Förklaras i martinskod.php.
?>
