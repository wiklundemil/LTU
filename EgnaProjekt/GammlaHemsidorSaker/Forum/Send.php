<?php

	include 'config.php';


	if(isset($_POST['password'])){

		$username = $_POST['username'];
		$password = $_POST['password'];
	}
	else{

		$password ="";
		$username="";
	}
		
	
	$hash = password_hash($password, PASSWORD_BCRYPT, array('password' => 'password'));	

	$stmt = $dbh->prepare('SELECT * FROM account WHERE username =:username');

	//$stmt ->execute(['password' => $password, 'username' => $username]);

	$sucss = $stmt->execute(array('username'=>$username));	
	
	$result = $stmt->fetchAll();
	foreach($result as $row){


	if(password_verify($password, $row['password'])){

	session_start();
	$_SESSION['username'] = $username;
	$_SESSION['inloggad'] = true;
	$_SESSION['role'] = $row['role'];

	header('Location:Start.php');	

	}
					
	else{
		
		echo"Oj tror det gick lite fort där.";
		 		
	}



	
}
/*
	$HeadAdmin = "HeadAdmin";
	$Admin = "Admin";
	$Moderator = "Moderator";
		
	$stmt = $dbh->prepare("SELECT role FROM account WHERE username =:'t'");
	$sucss = $stmt->execute(array('username'=>$username));	

	//$stmt ->execute(['password' => $password, 'username' => $username]);
	$result = $stmt->fetchAll();
	foreach($result as $row){

	if($row == $HeadAdmin){

		echo "hej HeadAdmin!";

	}
	else{

		echo "Nästan där!";
	}
}
*/
?>