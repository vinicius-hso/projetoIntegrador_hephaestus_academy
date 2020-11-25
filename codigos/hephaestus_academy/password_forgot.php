<?php include 'includes/session.php'; ?>
<?php include 'includes/header.php'; ?>
<body class="hold-transition login-page">
  <?php include 'includes/navbar.php'; ?>

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
        <p class="login-box-msg">Digite o seu email associado a conta</p>

        <form action="reset.php" method="POST">
            <div class="form-group has-feedback">
              <input type="email" class="form-control" name="email" placeholder="Email" required>
              <span class="glyphicon glyphicon-envelope form-control-feedback"></span>
            </div>
            <div class="row">
            <div class="col-xs-4">
                  <button type="submit" class="btn btn-primary btn-block btn-flat" name="reset"><i class="fa fa-mail-forward"></i> Enviar</button>
              </div>
            </div>
        </form>
        <br>
        <a href="login.php">Me lembrei da senha</a><br>
        <a href="index.php"><i class="fa fa-home"></i> Home</a>
      </div>
  </div>

	<?php include 'includes/footer.php'; ?>
  
  <?php include 'includes/scripts.php' ?>
</body>
</html>
