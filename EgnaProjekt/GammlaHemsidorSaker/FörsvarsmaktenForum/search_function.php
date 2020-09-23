<?php
	
	include'config.php';

	if(isset($_GET['search'])){

		$search = $_GET['search']."%";
	
	}	
	else{

		$search="Null";
	
	}	
	
	$category = $_GET['category'];

	if(isset($_GET['category'])){

	$stmt = $dbh->prepare('SELECT * FROM threads WHERE thread_name LIKE :search AND thread_category LIKE :category');	
	$stmt->bindValue(':search', $search);
	$stmt->bindValue(':category', $category);
	$stmt->execute();
 	
	$result = $stmt->fetchAll();
	foreach($result as $r){

		echo "<br><br><center>" ."<a action='thread' href='?id=". $r['id']."'>" . $r['thread_name']."</a></center>";
	
	}
}
	if(!isset($_GET['category'])){

		$_GET['category'] = "%";

	}

?>