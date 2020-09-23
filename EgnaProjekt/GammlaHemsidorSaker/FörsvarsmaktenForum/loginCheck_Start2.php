		
		<?php
		session_start();
		if(!isset($_SESSION['inloggad'])){
		
		include'buttons_login.php';
		}
		else{

		}

		if(isset($_SESSION['inloggad'])){
		
			echo "Inloggad!";	
			$profilePicture ='<a href="MyProfile.php"> <div id="avatar"></div></a>'.'<center>'.$_SESSION['username'];
			echo $profilePicture;
    		include'logout.php';

		}
		else{


		}
		?>
