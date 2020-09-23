<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Försvarsmakten</title>
        <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">
    <style>
        body {
            font-family: "proxima-nova", sans-serif;
            font-size: 16px;
        }
        
        body a {
            color: inherit;
            text-decoration: none;
        }
        
        .left {
            float: left;
        }
        
        .right {
            float: right;
        }
        
        header:after,
        .login-form:after,
        footer:after {
            display: table;
            clear: both;
        }
        
        .ui-panel {
            margin: 0 auto;
            margin-top: 120px;
            width: 360px;
            height: auto;
            background-color: black;
            color: white;
            border: 1px solid #161616;
            box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.3);
            position: absolute;
            margin-top: -130px;
            margin-left: -181px;
            top: 30%;
            left: 50%;
        }
        
        header {
            height: 46px;
            border-bottom: 1px solid #161616;
            line-height: 46px;
            padding: 0 28px;
            font-size: 0.65em;
            font-weight: 600;
            letter-spacing: 0.3em;
        }
        
        header .logo {
            text-transform: uppercase;

        }
        
        header span {
            color: #ffff11;
        }
        header span1 {
            color: #00bdfc;
        }
        
        .login-form {
            padding: 18px 28px 0 28px;
        }
        
        .login-form .subtitle {
            font-size: 0.92em;
        }
        
        .login-form input {
            font-size: 1.05em;
            font-weight: 300;
            margin-top: 18px;
            padding: 10px 8px;
            width: 288px;
        }
        
        footer {
            padding: 26px 28px 22px 28px;
            font-size: 0.82em;
        }
        
        footer .social-login i:first-child {
            margin-left: 4px;
        }
        


        footer .form-actions a {
            padding: 4px 8px;
        }
        
        footer .register {
            background-color: #ffff11;
            color: black;
            border-radius: 2px;
        }
        
        body {
            width: 100%;
            height: 100%;
            -webkit-background-size: cover;
            -moz-background-size: cover;
            -o-background-size: cover;
            background-size: cover;
        }
        
        .overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.88);
        }
    </style>

</head>

<body>

    <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">

    <link href="https://s3-us-west-2.amazonaws.com/s.cdpn.io/67239/animate.min.css" rel="stylesheet" />

    <div class="body"></div>

    <div class="overlay">
        <div class="ui-panel login-panel animated bounceInDown">
            <header>
                <div class="left logo">

                    <a href="logo"><span>Försvars</span><span1>makten</span1></a>
                </div>

                <div class="right">
                    <a href="#close" id="close" class="ui-button close">
                    </a>
                </div>
            </header>

            <div class="login-form">
                <div class="subtitle">Skapa ett nytt konto</div>
                <form action="NewUser.php" method="post">

                 <input type="text" name="name" placeholder="Förnamn*" >
                  <input type="text" name="surname" placeholder="Efternamn*" >
                <input type="text" name="newuser" placeholder="Användarnamn*" >
                <input type="password" name="newpassword" placeholder="Lösenord*" >
                 <input type="text" name="passwordcheck" placeholder="Bekräfta Lösenord" >
                <input type="text" name="email" placeholder="E-mail*" >
                <input type="text" name="phonenumber" placeholder="Mobilnummer">
                <input type="submit" name="submit" value="Registrera">

                </form>
            </div>

            <footer>
                <div class="right form-actions">
                    <a href="#register" class="button for register">Registrera</a>
                </div>
            </footer>
        </div>
    </div>
</body>

</html>

<!--

	Filen 1/2 till registreringssidan, koden skapar ett formulär som sedan skickas vidare till NewUser.php filen. Koden länkas ifrån buttons_login.php. 

-->