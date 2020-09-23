<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Försvarsmakten</title>

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
            content: "";
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
            top: 50%;
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
            background-color: #ffdd00;
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
                    <a href="#logo"><span>Försvars</span><span1>makten</span1></a>
                </div>

                <div class="right">
                    <a href="#close" id="close" class="ui-button close">
                    </a>
                </div>
            </header>

            <div class="login-form">
                <div class="subtitle">Login or register</div>
                <form action="send.php" method="post">
                <input type="text" name="username" placeholder="Username"/>
                <input type="text" name="password" placeholder="Password"/>
                <input type="submit" name="login" value="Login">                
                </form>
            </div>
            <footer>
                <div class="right form-actions">
                    <a href="login" class="button for login">Login</a>
                    <a href="register.html" class="button for register">Register</a>
                </div>
            </footer>
        </div>
    </div>
</body>

</html>