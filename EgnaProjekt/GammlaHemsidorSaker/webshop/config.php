
<!-- Uppkoppling localt -->

<?php

$dbh = new PDO('mysql:host=localhost;dbname=webshop', 'root','',array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES 'utf8'"));

?>

<!--

    Uppkoppling online

<?php

   /* //try{
        $dbh = new PDO('mysql:host=my148b.sqlserver.se;dbname=198526-recipes',
                        '198526_pm78428',
                        'admin123',
                        array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES 'utf8'"));


        $dbh = new pdo( 'mysql:host=my148b.sqlserver.se;dbname=198526-forsvarsmakten',
                        '198526_xs17122',
                        'admin123',
                        array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
        die('Ansluten');
}

catch(PDOException $ex){
    die('Fel');
}*/

?>
-->