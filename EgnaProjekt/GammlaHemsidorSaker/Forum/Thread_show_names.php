<?php

	include 'config.php';
	
	if(isset($_GET['id'])){
    	
    	$threadid = $_GET['id'];
	
	}
	else{
    
    	$threadid = "%";
	
	}
	
	$stmt = $dbh->prepare('SELECT * FROM threads ORDER BY thread_likes DESC LIMIT 7');
	$stmt->execute( array());

	$result = $stmt->fetchAll();
	foreach($result as $r)
	{

 	   echo "<br><br><center><a action='thread' href='?id='". $threadid."><div class='popularthreads'><div class='alignment_threads'>[". $r['thread_name']."]</a></div></div></center><br><br>";
    	$upvotes = $r['thread_likes'];

	}

	//Koden skriver ut alla trådar, mer förklarae i martinskod.php.
?>
