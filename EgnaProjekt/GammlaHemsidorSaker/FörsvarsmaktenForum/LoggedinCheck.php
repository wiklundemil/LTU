<link rel="stylesheet" type="text/css" href="Style.css">
<?php 
	include'config.php';
    $stmt = $dbh->prepare("SELECT * FROM account");
	
	$welcomeText = '<div id="welcometext">Welcome to this site'.' '.''.' '.$_SESSION['username']. '!'. '</div>';

	if($_SESSION['inloggad']){
		
	echo $welcomeText;

	}
	else{

	}
	
?>