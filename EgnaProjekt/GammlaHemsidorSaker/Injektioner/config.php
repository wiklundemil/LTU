<?php
	try {

		$dbh = new PDO('mysql:host=localhost; dbname=sqltraining', 'root', '',array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES 'utf8'"));
		$dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	}
	 catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
} 
