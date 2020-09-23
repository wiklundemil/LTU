<?php
	
	include 'config.php';

	$username = $_POST['newuser'];
	$password = $_POST['newpassword'];
	$name = $_POST['name'];
	$surname = $_POST['surname'];
	$passwordcheck = $_POST['passwordcheck'];


	$password = password_hash($password, PASSWORD_DEFAULT);	
	$salt = rand();

	$hashedsalt = password_hash($salt, PASSWORD_DEFAULT);

	$phonenumber = $_POST['phonenumber'];
	$email = $_POST['email'];

	$stmt = $dbh->prepare("INSERT INTO account VALUES('$hashedsalt', '$name', '$surname', '$username','bild.exe was not found', '$password', '$passwordcheck', '$phonenumber', '$email', '0')");
	$inset = $stmt->execute();

	if($inset){

		echo "Succses!";
		sleep(0.5);
		header('Location:Start.php');

	}
	else{
	
		echo"Nae";
	
	}
?>

<!--

	Filen 2/2 av registreringssidan. Filens jobb är att lägga till en ny användare. Koden länkas ifrån NewUSer_form.php. 

-->