<center>
	
	<br>
	<br>

	<form action="Threads_New.php" method="post">

		<input type="text" name="NewThread" placeholder="Name your thread" required>

		<input type="submit" name="new" value="New Thread">
		
		<br>
		
		<select name="category" value="category">

			<option value="category" disabled selected>Kategori</option>
			<option value="marinen">Marinen</option>
			<option value="armen">Armén</option>
			<option value="flygvapnet">Flygvapnet</option>	

		</select>
	
	</form>
	
	<br>
</center>

<!-- Kategorie val när man skapar en ny tråd. -->