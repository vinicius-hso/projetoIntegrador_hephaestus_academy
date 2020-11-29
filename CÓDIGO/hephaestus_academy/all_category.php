<?php include 'includes/session.php'; ?>
<?php
  $where = '';
  if(isset($_GET['category'])){
    $catid = $_GET['category'];
    $where = 'WHERE category_id ='.$catid;
  }

?>
<?php include 'includes/header.php'; ?>

<body class="hold-transition skin-blue layout-top-nav">
<div class="wrapper">

	<?php include 'includes/navbar.php'; ?>
	<div class="div-promocao">
		<a class="div-promocao" href="promocao.php">Na compra de um conteúdo, GANHE GRÁTIS UM JOGO PARA AVALIAR SEUS CONHECIMENTOS!</a>
	</div>
	 
	  <div class="height-adjust content-wrapper">
	    <div class="container">

	      <!-- Main content -->
	      <section class="content">
	        <div class="row">
	        	<div class="col-sm-9">
	        		<?php
		       			
		       			$conn = $pdo->open();    			

		       			try{
		       				$stmt1 = $conn->prepare("SELECT * FROM category $where");
		       				$stmt1->execute();		       				
							foreach ($stmt1 as $row1){		            			
		            			echo "
		            			<div class='container'> 
		            			<h1 class='page-header product-header'>".$row1['name']."</h1></div>";
		       		
			       			 	$inc = 3;
			       			 	$catid = $row1['id'];
							    $stmt = $conn->prepare("SELECT * FROM products WHERE category_id = :catid");
							    $stmt->execute(['catid' => $catid]);
							    foreach ($stmt as $row) {
							    	$image = (!empty($row['photo'])) ? 'images/'.$row['photo'] : 'images/noimage.jpg';
							    	$inc = ($inc == 3) ? 1 : $inc + 1;
		       						if($inc == 1) echo "<div class='row'>";
		       						echo "
		       							<div class='col-sm-4'>
		       								<div class='card card-products box box-solid'>
			       								<div class='box-body prod-body'>
			       									<img src='".$image."' width='100%' height='230px' class='thumbnail'>
			       									<h6><b><a href='product.php?product=".$row['slug']."'>".$row['name']."</a></b></h6>
			       								</div>
			       								<div class='card-footer'>
			       									<b>R&#36; ".number_format($row['price'], 2)."</b>
			       								</div>
		       								</div>
		       							</div>
		       						";
		       						if($inc == 3) echo "</div>";
							    }
							    echo "<div class='container'><br/><br/></div>";
							}
						    if($inc == 1) echo "<div class='col-sm-4'></div><div class='col-sm-4'></div></div>"; 
							if($inc == 2) echo "<div class='col-sm-4'></div></div>";
						}
						catch(PDOException $e){
							echo "Há algum problema de conexão: " . $e->getMessage();
						}

						$pdo->close();

		       		?> 
	        	</div>
	        	<div class="col-sm-3">
	        		
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
