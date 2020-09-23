<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js%22%3E"></script>
<script>
function upvoted(id, likes){

        likes++;


        $.ajax({
        url: 'LikeFunction.php',
        type: 'post',
        data: 'thread_likes='+likes+'&id='+id,
        success: function(output) 
        {

        }, error: function()
        {
        // alert('something went wrong, rating failed');
        }
        });
        location.reload();
}

</script>


    <?php

    include 'config.php';

    if(isset($_POST['id'])){

                $id = $_POST['id'];
                $likes = $_POST['thread_likes'];
            }
            else{

                $id ="";
                $likes="";
            }

        $stmt = $dbh->prepare("UPDATE `threads` SET thread_likes=:likes WHERE threads.id=:id");

        $stmt->execute(array('likes'=>$likes, 'id'=>$id));
        ?>