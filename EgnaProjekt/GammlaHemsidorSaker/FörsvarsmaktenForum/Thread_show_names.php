<?php

	include 'LikeFunction.php';
	include 'config.php';
	
	if(isset($_GET['id'])){
    	
    	$threadid = $_GET['id'];
	
	}
	else{
    
    	$threadid = "%";
	
	}
	
	$stmt = $dbh->prepare('SELECT * FROM threads ORDER BY thread_likes DESC');
	$stmt->execute( array());

	$result = $stmt->fetchAll();
	foreach($result as $r)
	{

 	   echo "<br>". "<center>" ."<a action='thread' href='?id='". $r['id'].">".'<h4>'. $r['thread_name'].'</h4>' . '</a>'.'<br>';
    	$upvotes = $r['thread_likes'];
    	include'delete.php';	    

	}

	//Koden skriver ut alla trådar, mer förklarae i martinskod.php.
?>
