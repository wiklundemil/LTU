<?php 

	if(isset($_GET['hot'])){

	    include'1.php';

	}
	else if(isset($_GET['newprices'])){

		include'2.php';
	}

	if(isset($_GET['clips'])){

		include'3.php';
	}
?>