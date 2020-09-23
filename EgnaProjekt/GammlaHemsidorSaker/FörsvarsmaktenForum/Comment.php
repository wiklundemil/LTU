<?php

	include 'config.php';
	
	if(isset($_GET['id'])){

    	$threadid = $_GET['id'];
	
	}
	else{

   		$threadid = "48";
	
	}

	if(isset($_POST['newcomment'])){

		$comment = $_POST['newcomment'];
		$date = date("Y-m-d H:i:s");

		$stmt = $dbh->prepare("INSERT INTO comments VALUES(NULL, '$comment', :pubdate, 'author', :threadid)");
		$stmt->bindValue(':pubdate', $date);
		$stmt->bindValue(':threadid', $threadid);
		
		$inset = $stmt->execute();

		if($inset){
			$link = "Location:martinskod.php?id=".$_POST['thread_id'];
			echo "Succses!";
			header($link);
		}
		else{
	
			echo"Nae";
	
		}
	}
	else{

	echo"teststop";

	}

?>

