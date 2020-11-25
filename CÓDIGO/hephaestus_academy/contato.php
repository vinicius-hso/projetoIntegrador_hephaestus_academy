<?php include 'includes/session.php'; ?>
<?php include 'includes/header.php'; ?>
<body class="hold-transition skin-green layout-top-nav">
<div>

	<?php include 'includes/navbar.php'; ?>
	 


	<!-- Main content -->
	<main role="main">
	    <!-- Main jumbotron for a primary marketing message or call to action -->
	    <div class="height-adjust">
			<!-- Contato -->
	    	<div class="div-contato">
				<h1>Contato</h1>
				<hr>
				<form action="/definir_a_ação">
					<div class="form-group">
						<label for="userControlInput1">Nome:</label>
    					<input type="text" class="form-control" id="userControlInput1" placeholder="nome" required>
					</div>
					<div class="form-group">
						<label for="FormControlInput1">Email:</label>
						<input type="email" class="form-control" id="FormControlInput1" placeholder="nome@email.com" required>
					</div>
					<div class="form-group">
						<label for="textoFormControlTextarea1">Mensagem:</label>
						<textarea class="form-control" id="exampleFormControlTextarea1" rows="4" placeholder="Fale conosco" required></textarea>
					</div> 
					<div class="form-group">
						<button type="button" class="btn btn-success">Enviar</button>
					</div>
					<hr>
					<div id="div-logo">
						<a class="logo" href="https://facebook.com">
							<img src="images/facebook.png" alt="" style="width: 30px;">
						</a>
						<a class="logo" href="https://instagram.com">
							<img src="images/instagram.png" alt="" style="width: 30px;">
						</a>
						<a class="logo" href="https://twitter.com">
							<img src="images/twitter.png" alt="" style="width: 30px;">
						</a>
					</div>
					
				</form>

			</div>
			<!-- Contato -->
		</div>
		
	</main>
  
  	<?php include 'includes/footer.php'; ?>
</div>

<?php include 'includes/scripts.php'; ?>
</body>
</html>