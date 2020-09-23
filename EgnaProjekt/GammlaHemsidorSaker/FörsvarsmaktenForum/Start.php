<link rel="stylesheet" type="text/css" href="style.css">

<a href="martinskod.php">Threads</a>

<center>
	<?php

		session_start();

		if(isset($_SESSION['inloggad'])){
			
			include'LoggedinCheck.php';
			include'Roles.php';
		
		}
	?>
</center>

<!--

	Koden skapar en ny blank sida som importerar Välkomst text 'OM' man är inloggad. Koden ligger som en egen fil. 

-->