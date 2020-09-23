<?php
    
    include 'LikeFunction.php';
    include 'config.php';

    if(!isset($_GET['search'])){


        if(isset($_GET['id'])){

            include'Comment_form.php';

            $threadid = $_GET['id'];
        
        }
        else{
        
            $threadid = "%";

        }


        $stmt = $dbh->prepare('SELECT * FROM threads WHERE id  LIKE :threadid ORDER BY thread_likes DESC LIMIT 10');

        $stmt->execute(array('threadid' => $threadid));

        $result = $stmt->fetchAll();
        foreach($result as $r)
        {

            echo "<center> <div class='threads'><br><a action='thread' href='?id=". $r['id']."'>" . $r['thread_name']."</a></div></center>";
            include'Uppvote_button.php'; 
    
            $upvotes = $r['thread_likes'];
     
        }
    }
?>
