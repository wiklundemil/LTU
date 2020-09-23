<?php
	
	include 'config.php';

	$id = $_POST['id'];
	$thread_likes = $_POST['thread_likes'];

	$stmt = $dbh->prepare("UPDATE threads SET thread_likes=:likes WHERE threads.id=:id");
	$inset = $stmt->execute( array('thread_likes'=>$likes, 'id'=>$id));

?>