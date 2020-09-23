<?php
	//$id = 'id';
	//$thread_name = $_POST['thread_name'];
	
	//$stmt = $dbh->prepare("SELECT id FROM threads WHERE thread_name =:'thred_name'");

	include 'config.php';

	$knapptryck = $_POST['knapptryck'];
	
	if(isset($_GET['id'])){
    $threadid = $_GET['id'];
	
	}
else{
    $threadid = "%";
}

	$stmt = $dbh->prepare("UPDATE `account` SET `knapptryck` =:knapptryck WHERE `account`.`id` = $id");
	$inset = $stmt->execute( array('knapptryck' => $knapptryck));

	if($inset){

	echo "Succses!";
	

}
else{
	echo"Nae";
}

?>

