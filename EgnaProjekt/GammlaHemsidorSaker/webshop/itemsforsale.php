<?php
	
	include'config.php';


    $stmt = $dbh->prepare("SELECT * FROM item ORDER BY itemid ASC");
    $stmt->execute();
	

    $result = $stmt->fetchAll();
    foreach($result as $r)
    {

        echo "<center><div class='grid-item'>" . $r['name'] . "<br/>" . $r['price'] . "kr" . "<br/>" . $r['description'] . "<br/><br/>" . "</div></center>";

    }

?>