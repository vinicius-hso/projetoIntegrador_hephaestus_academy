<?php include 'includes/session.php'; ?>
<?php
	$output = '';
	if(!isset($_GET['code']) OR !isset($_GET['user'])){
		$output .= '
			<div class="alert alert-danger">
	            <h4><i class="icon fa fa-warning"></i> Erro!</h4>
	            Código para ativar a conta foi achado.
	        </div>
	        <h4>Você pode <a href="signup.php">Entrar</a> ou voltar para a <a href="index.php">Homepage</a>.</h4>
		'; 
	}
	else{
		$conn = $pdo->open();

		$stmt = $conn->prepare("SELECT *, COUNT(*) AS numrows FROM users WHERE activate_code=:code AND id=:id");
		$stmt->execute(['code'=>$_GET['code'], 'id'=>$_GET['user']]);
		$row = $stmt->fetch();

		if($row['numrows'] > 0){
			if($row['status']){
				$output .= '
					<div class="alert alert-danger">
		                <h4><i class="icon fa fa-warning"></i> Erro!</h4>
		                Conta já está ativada.
		            </div>
		            <h4>Você pode <a href="login.php">Entrar</a> ou voltar para a <a href="index.php">Homepage</a>.</h4>
				';
			}
			else{
				try{
					$stmt = $conn->prepare("UPDATE users SET status=:status WHERE id=:id");
					$stmt->execute(['status'=>1, 'id'=>$row['id']]);
					$output .= '
						<div class="alert alert-success">
			                <h4><i class="icon fa fa-check"></i> Conta Ativada com Sucesso!</h4>
			                Conta ativada - Email: <b>'.$row['email'].'</b>.
			            </div>
			            <h4>Você pode <a href="login.php">Entrar</a> ou voltar para a <a href="index.php">Homepage</a>.</h4>
					';
				}
				catch(PDOException $e){
					$output .= '
						<div class="alert alert-danger">
			                <h4><i class="icon fa fa-warning"></i> Erro!</h4>
			                '.$e->getMessage().'
			            </div>
			            <h4>Você pode <a href="signup.php">Entrar</a> ou voltar para a <a href="index.php">Homepage</a>.</h4>
					';
				}

			}
			
		}
		else{
			$output .= '
				<div class="alert alert-danger">
	                <h4><i class="icon fa fa-warning"></i> Erro!</h4>
	                Não é possível ativar sua conta. Código incorreto.
	            </div>
	            <h4>Você pode <a href="signup.php">Entrar</a> ou voltar para a <a href="index.php">Homepage</a>.</h4>
			';
		}

		$pdo->close();
	}
?>
<?php include 'includes/header.php'; ?>
<body class="hold-transition layout-top-nav">
<div class="wrapper">

	<?php include 'includes/navbar.php'; ?>
	 
	  <div class="height-adjust content-wrapper">
	    <div class="container">

	      <!-- Main content -->
	      <section class="content">
	        <div class="row">
	        	<div class="col-sm-9">
	        		<br/><br/><br/><br/><br/><br/>
	        		<?php echo $output; ?>
	        		<br/><br/><br/><br/><br/><br/>
	        	</div>
	        	
	        </div>
	      </section>
	     
	    </div>
	  </div>
  
  	<?php include 'includes/footer.php'; ?>
</div>

<?php include 'includes/scripts.php'; ?>
</body>
</html>