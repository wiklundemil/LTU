<link rel="stylesheet" type="text/css" href="Style_övrigt.css">    
<link rel="stylesheet" type="text/css" href="thread_categorysites.css">
<link rel="stylesheet" type="text/css" href="menu.css">

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

		
<div id="searchbar-meny">
    <form action="" autocomplete="on">
	  	<input id="search" name="search" type="text" placeholder="Sök efter en tråd..."><i class="fa fa-search fa-2x"></i>
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
<div class="newthread_form">

	<center><h1>New thread<h1></center>
	
	<div id="searchbar-meny2">
	    <form action="" autocomplete="on">
		
	  		<input id="search" name="search" type="text" placeholder="Namn på ny tråd..."><i class="fa fa-plus-square fa-2x"></i>
		   
	    </form>
	</div>

	<div class="yourthreads">
		
		<?php

			include 'config.php';
				
			if(isset($_SESSION['username'])){

				
				if(isset($_GET['id'])){
			    	
			    	$threadid = $_GET['id'];
				
				}
				else{
			    
			    	$threadid = "%";
				
				}
				$author = $_SESSION['username'];

				$stmt = $dbh->prepare('SELECT * FROM threads WHERE thread_author =:author ORDER BY thread_likes DESC');
				$stmt->bindvalue(':author', $author);
				$stmt->execute();

				$result = $stmt->fetchAll();
				foreach($result as $r)
				{

			 	   echo "<br>". "<center><div class='threads'>" ."<a action='thread' href='?id='". $r['id'].">". $r['thread_name'].'</a></div>'.'<br>';

				}
			}
			if(!isset($_SESSION['username'])){

				echo"<center>Att skapa trådar går endast att göra när du är inloggad.</center>";
			
			}
		?>
	</div>
</div>
<?php
	
	if(isset($_GET['id'])){
    	
    	$threadid = $_GET['id'];
	
	}
	else{
    
    	$threadid = "%";
	
	}

	include'config.php';

	$stmt = $dbh->prepare("SELECT * FROM threads WHERE thread_category =:category");
	$stmt->bindvalue(':category',"hemvärnet");
	$stmt->execute();

	$result = $stmt->fetchAll();
	foreach($result as $r)
	{

 	   echo "
 	   			<center>

 	   				<a action='thread' href='?id='".$threadid."'>

 	   					<div class='grid-item'>

							<div class='alignment_threads'>".$r['thread_name']."</div>
 	   						
 	   						<div class='uploadedby'>Created by: Eric</div>

 	   					</div>
 	   				
 	   				</a>
 	   			
 	   			</center>";

	}

?>