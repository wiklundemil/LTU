
<link rel="stylesheet" type="text/css" href="style_martin.css">


<div class="profilepicture">
	<center>	
		
		<?php
			session_start();
			if(!isset($_SESSION['inloggad'])){
		
				include'buttons_login.php';
		
			}
			else{
			
			}

			if(isset($_SESSION['inloggad'])){
		
				echo "Inloggad!";	
				$profilePicture ='<a href="MyProfile.php"> <div id="avatar_myprofile"></div></a>'.$_SESSION['username'];
				echo $profilePicture;
    			include'logout.php';

			}
			else{

			}
		?>

	</center>
</div>