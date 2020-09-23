<?php
	
	include'search_function.php';
	include 'config.php';

	$thread_name = $_POST['NewThread'];
	$thread_picture = "test.png";
	$thread_comment = "test";
	$thread_likes = 0;
	$thread_category = $_POST['category'];

	$stmt = $dbh->prepare("INSERT INTO threads VALUES(NULL, '$thread_name', '$thread_picture', '$thread_category', '$thread_likes', '$thread_comment')");
	$inset = $stmt->execute();

	if($inset){

	$_SESSION['id'] = 'id';
	header('Location:martinskod.php');

}
else{
	echo"Nae";
}
?>