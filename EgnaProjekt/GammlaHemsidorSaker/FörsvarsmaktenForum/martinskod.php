<!DOCTYPE html>
<html>
<head>
    
    <link rel="stylesheet" type="text/css" href="style_martin.css">
    <link rel="icon" href="favicon.ico" type="favicon.png"/>

</head>
    <body>
        <div>
            <div class="menu">
                <a href="Start.php">
                    <img src="försvarsmakten.png">
                </a>

            <!-- Koden visar försvarsmaktens logga, om man klickar på den länkas man till Start.php. Koden är en grunden till tråd sidan. -->

                <div class="links">
                    <a href="Start.php">
                        HEM
                    </a>

                    <a href="#">
                        ANNAT
                    </a>

                </div>

        <!-- Koden skapar länkar runt HEM och ANNAT i menyn. -->
                <div>
                    <class id="login">
    
                        <?php include'buttons_check.php'; ?>

                    </div>
        <!-- Koden skapar login och registrerings knappar. Filen länkar till buttons_check.php, buttons_check.php kollar om man är inloggad eller inte och bestämmer om knapparna ska skrivas ut eller inte. Alternativt om man nu är inloggad så byts knapparna ut till din avatar bild och ditt namn. -->            
                </class>
            </div>
        </div>
    </div>

    <div class="sida">
        <div class="nytråd">
            <center>

                <?php
     
                    include'Thread_notloggedin.php';     
     
                ?>
     
            </center>
        </div>
        <!-- Koden kollar om du är inloggad, om du inte är det så skrivs ett medelande att du itne kan se just dina trådar. Du kan också inte skapa nya trådar när du är utloggad. -->
    </div>
    <div class="trådar">
        <div class="searchchoises">

        <!-- Searchchoises är den klassen som sammlar olika sökfunktioner. -->

            <div class="content2">
                <center>
                
                    <?php
    
                        include'Search.php';
        
                    ?>
    
                </center>  
            </div>
            <!-- Sök och kategorival. -->
        </div>
        <div class="trådfunktioner">
      
            <?php
        
                include'Thread_show.php';
        
            ?>
    
        </div>
        <!-- Koden visar 'alla' tråder. -->
    </div>
</body>
</html>