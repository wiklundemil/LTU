<!DOCTYPE html>
<html>
	<head>

		<title>Forum Gränssnitt</title>

		<meta charset="utf-8">

    <link rel="stylesheet" type="text/css" href="menu.css">
    <link rel="stylesheet" type="text/css" href="grid.css">
    <link rel="stylesheet" type="text/css" href="threads.css">
    <link rel="stylesheet" type="text/css" href="socailmedia.css">
    <link rel="stylesheet" type="text/css" href="Style_övrigt.css">    

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

	</head>
	<body>	
		
		<div id="searchbar-meny">
		    <form action="" autocomplete="on">
		
		  		<input id="search" name="search" type="text" placeholder="Söka efter en tråd..."><i class="fa fa-search fa-2x"></i>
		   
		    </form>
		</div>
				
		<div id="meny">
			<a href="Start.php">
				<img src="Försvarsmakten.png">
			</a>
		</div>
			
		<div class="login">
			<?php 
		        session_start();

		        if(!isset($_SESSION['inloggad'])){ 
		         
		            include'buttons_login.php';
		            include'ifnotinloggad_sök.php';
		         
		        }
		        if(isset($_SESSION['inloggad'])){

		            include'Logout.php';
		            include'ifinloggad_sök.php';

		        }
		    ?>

		</div>
		
		<div id="lista">
			<div class="låda-för-trådar">	
				<div class="låda-för-trådar-content">
					<center><h1>Heta trådar</h1></center>
					<br>
					<?php
						include'thread_show_names.php';
					?>
				</div>		
			</div>
		</div>
	
			<div id="grid-container">
  				<div class="grid-item">
  					<a href="armen.php">
              <img src="armén.jpg">
  					  <div class="overlay">
  						  <div class="text">Armén</div>
  						  </div>
  					  </a>
  				  </div>
				
  				<div class="grid-item">
  					<a href="marinen.php">
              <img src="marinen.jpg">
  						<div class="overlay">
  			
  							<div class="text">Marinen</div>
  			
  						</div>
  					</a>
  				</div>

  				<div class="grid-item">
  					<a href="flygvapnet.php">
              <img src="flygvapnet.jpg">
  						<div class="overlay">
  			
  							<div class="text">Flygvapnet</div>
  			
  						</div>
  					</a>
  				</div>
				
  				<div class="grid-item">
  					<a href="högvakten.php">
              <img src="högvakten.jpg">
  						<div class="overlay">
  			
  							<div class="text">Högvakten</div>
  			
  						</div>
  					</a>
  			 	</div>
				
  				<div class="grid-item">
  					<a href="logistik.php">
              <img src="logistik.jpg">
  						<div class="overlay">
  			
  							<div class="text">Logistik</div>
  			
  						</div>
  					</a>
  				</div>
				
  				<div class="grid-item">
  					<a href="hemvärnet.php">
              <img src="hemvärnet.png">
  						<div class="overlay">
  			
  							<div class="text">Hemvärnet</div>
  			
  						</div>
  					</a>
  				</div>		
			</div>
		<div class="socialamedier">
			<div class="socialamedier-content">

				Instagam: <a href="https://www.instagram.com/forsvarsmakten/?hl=sv">@forsvarsmakten</a>
				<br>
				<br>
				<br>
				Facebook: <a href="https://www.facebook.com/forsvarsmakten">@Försvarsmakten</a>
				<br>
				<br>
				<br>
				Twitter: <a href="https://twitter.com/forsvarsmakten">@forsvarsmakten</a>
				<br>
				<br>
				<br>
				E-post: exp-hkv@mil.se

			</div>
		</div>
	</body>
</html>