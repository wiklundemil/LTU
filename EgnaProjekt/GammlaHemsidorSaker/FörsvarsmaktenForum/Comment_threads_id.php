<?php
	
	include 'config.php';
header('Location:Comment.php');
	$id =$_POST['id'];

	$stmt = $dbh->prepare("SELECT id FROM threads");
	$inset = $stmt->execute( array('id' => $id));

	if($inset){

		header('Location:Comment.php');

}
else{
	echo"Nae";
}

?>