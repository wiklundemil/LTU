<?php
	
	include('config.php');

	if(isset($_GET['id'])){

	    $threadid = $_GET['id'];
	
	}
	else{
    	
    	$threadid = "";
	
	}
	
	$sql = $dbh->prepare('DELETE FROM threads WHERE id =:id');
	$sql -> execute(array('id' => $threadid));

	header('Location:martinskod.php');

?>

<!-- Koden ska ta bort ett inlägg, filen kommer att includeras i filen Thread_show_names.php. -->