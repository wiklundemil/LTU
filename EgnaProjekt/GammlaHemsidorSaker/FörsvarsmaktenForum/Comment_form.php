<?php echo '<form action="Comment.php?id='. $_GET['id'].'" method="post">';?>

	<input type="hidden" name="thread_id" value="<?php echo $_GET['id']; ?>">

	<input type="text" name="newcomment" placeholder="Förnamn">

	<input type="submit" name="submit">
	
</form>