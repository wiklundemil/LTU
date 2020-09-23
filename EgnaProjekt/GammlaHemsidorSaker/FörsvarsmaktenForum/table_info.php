<br>
<br>
<br>

<div class="info_roles">

User = 0<br>
Moderator = 1<br>
Admin = 2<br>
HeadAdmin = 3

<br>
<br>
<br>
<br>
<br>

</div>
		<div class="table">
	
			<table>
											<tr>
					<td>

						 Username

					</td>

										<td>

						Phonenumber

					</td>
										<td>

						E-mail

					</td>

					<td>

						Role

					</td>
				</tr>
			
			<!-- Koden skapar en tabbel med rubrikerna ovanför. -->
	<?php
	
		include 'config.php';

		$stmt = $dbh->prepare("SELECT * FROM account");
		$stmt->execute();

		$result = $stmt->fetchAll();
		foreach($result as $r){
				echo "

				<tr>
					<td>".

						$r['username']

					."</td>
										<td>".

						$r['phonenumber']

					."</td>
										<td>".

						$r['email']

					."</td>

										<td>".

						$r['role']

					."</td>
										<td>".

						"<form action='role_update.php' method='post'>" . 

						"<input type='button' value='Moderator' name='knapptryck'>"."</input>"


						."</form></td><td>"
						.

						"<form action='role_update.php' method='post'>" . 

						"<input type='button' value='Admin' name='knapptryck'>"."</input>"


						."</form></td><td>"
						.

						"<form action='role_update.php' method='post'>" . 

						"<input type='button' value='HeadAdmin' name='knapptryck'>"."</input>"


						."</form></td><td>"
												.

						"<form action='role_update.php' method='post'>" . 

						"<input type='button' value='Demote to User' name='knapptryck'>"."</input>"


						."</form></td><td>"

					."</td>
				</tr>

				";
		}

	?>
			<!-- Koden skapar en tabbel med värderna och promote och demote kanppar ovanför. Koden includeras i Start.php. -->

				</table>
			</div>
	