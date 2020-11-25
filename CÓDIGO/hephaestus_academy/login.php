<?php include 'includes/session.php'; ?>
<?php
  if(isset($_SESSION['user'])){
    header('location: cart_view.php');
  }
?>
<?php include 'includes/header.php'; ?>

<body class="hold-transition login-page">

<?php include 'includes/navbar.php'; ?>

<div class="height-adjust">
  <main role="main">
    <div>
      <div class="login-box">
        <?php
          if(isset($_SESSION['error'])){
            echo "
              <div class='callout callout-danger text-center'>
                <p>".$_SESSION['error']."</p> 
              </div>
              ";
            unset($_SESSION['error']);
          }
          if(isset($_SESSION['success'])){
            echo "
              <div class='callout callout-success text-center'>
                <p>".$_SESSION['success']."</p> 
              </div>
            ";
            unset($_SESSION['success']);
          }
        ?>
         <div class="login-box-body">
            <p class="login-box-msg">Entre para iniciar sua sessão</p>

            <form action="verify.php" method="POST">
                <div class="form-group has-feedback">
                  <input type="email" class="form-control" name="email" placeholder="Email" required>
                  <span class="glyphicon glyphicon-envelope form-control-feedback"></span>
                </div>
                <div class="form-group has-feedback">
                  <input type="password" class="form-control" name="password" placeholder="Password" required>
                  <span class="glyphicon glyphicon-lock form-control-feedback"></span>
                </div>
                <div class="row">
                <div class="col-xs-4">
                      <button type="submit" class="btn btn-success btn-block btn-flat" name="login"><i class="fa fa-sign-in"></i> Entre </button>
                  </div>
                </div>
            </form>
            <br>
            <a href="password_forgot.php">Esqueci a senha</a><br>
            <a href="signup.php" class="text-center">Ainda não tenho conta</a><br>
            <a href="index.php"><i class="fa fa-home"></i> Home</a>
         </div>
      </div>
    </div>
    
  </main>  	
</div>
<?php include 'includes/footer.php'; ?>
<?php include 'includes/scripts.php' ?>
</body>
</html>
