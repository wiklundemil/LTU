<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Page Title</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" media="screen" href="css/main.css" />
        <script src="main.js"></script>
    </head>
    <body>
        <div class="top">
            <div id="topmenu">
                <div class="blackbar-menu">
                    <!-- <center>Om Emils Student</center> -->
                </div>
                <div class="rubrik"><center>Studenten 2019</center></div>
            </div>
        </div>
        <div class="middle">
            <div class="middlegrid">
                <div class="middlegrid-item"><img src="css/bilder/utspring.png" style="height:435px; width:630px;"></div>
                <div class="middlegrid-item"><img src="css/bilder/studentflak.png" style="height:435px; width:630px;"></div>
            </div>
        </div>
        <div class="footer"></div>
        <!-- Här ligger scriptfilen till topmenu -->
        <script type="text/javascript">
            var prevScrollpos = window.pageYOffset;
            window.onscroll = function(){
                var currentScrollpos = window.pageYOffset;
                if(prevScrollpos > currentScrollpos){
                    document.getElementById("topmenu").style.top="0";
                }else{
                    document.getElementById("topmenu").style.top="-100px";
                }
                prevScrollpos = currentScrollpos;
            }
        </script>
        <!-- Här ovan ligger scriptfilen till topmenu -->
    </body>
</html>
