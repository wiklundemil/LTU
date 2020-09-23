    <?php 
        if(!isset($_SESSION['inloggad'])){
        
            echo"Att lägga till eller visa dina trådar går bara när du är inloggad!";

        }
        else{

        }

        if(isset($_SESSION['inloggad'])){
        
           include'loginChecker_NewThread.php';
        include'Thread_show_names.php';
           

        }
        else{


        }
        
        //Koden förklaras i martinskod.php.
     ?>      