<?php include 'includes/session.php'; ?>
<?php
if(!empty($_GET['file']))
{
	$filename = basename($_GET['file']);
	$filepath = 'destination/' . $filename;
	if(!empty($filename) && file_exists($filepath)){

		//Definir Headers
		header("Cache-Control: public");
		header("Content-Description: File Transfer");
		header("Content-Disposition: attachment; filename=$filename");
		header("Content-Type: application/zip");
		header("Content-Transfer-Emconding: binary");

		readfile($filepath);
		exit;

	}
	else{
		echo "Esse arquivo não existe.";
	}
}
?>
<?php
	if(!isset($_SESSION['user'])){
		header('location: index.php');
	}
?>
<?php include 'includes/header.php'; ?>
<body class="hold-transition skin-blue layout-top-nav">
<div class="wrapper">

	<?php include 'includes/navbar.php'; ?>
	        <br/>
	        <br/>	 
	<div class="height-adjust content-wrapper">
	    <div class="container">
	      <!-- Main content -->
	    	<section class="content">
	        <div class="row">
	        	<div class="col-sm-9">
	        		<?php
	        			if(isset($_SESSION['error'])){
	        				echo "
	        					<div class='callout callout-danger'>
	        						".$_SESSION['error']."
	        					</div>
	        				";
	        				unset($_SESSION['error']);
	        			}

	        			if(isset($_SESSION['success'])){
	        				echo "
	        					<div class='callout callout-success'>
	        						".$_SESSION['success']."
	        					</div>
	        				";
	        				unset($_SESSION['success']);
	        			}
	        		?>
	        		<div class="box-body">
        				<table class="table table-bordered" id="example1">
        					<thead>
        						<th>Nome</th>
        						<th>Imagem</th>
        						<th>Descrição</th>	        						
        						<th>Baixar</th>
        					</thead>
        					<tbody>
        					<?php
        						$conn = $pdo->open();

        						try{
        							$stmt = $conn->prepare("SELECT * FROM sales WHERE user_id=:user_id ORDER BY sales_date DESC");
        							$stmt->execute(['user_id'=>$user['id']]);
        							foreach($stmt as $row){
        								$stmt2 = $conn->prepare("SELECT * FROM details LEFT JOIN products ON products.id=details.product_id WHERE sales_id=:id");
        								$stmt2->execute(['id'=>$row['id']]);
        								$total = 0;
        								foreach($stmt2 as $row2){  
        								$image2 = (!empty($row2['photo'])) ? 'images/'.$row2['photo'] : 'images/noimage.jpg';      								
	        								echo "
	        									<tr>
	        										<td><b>".$row2['name']."</b></td>
	        										<td><img src='".$image2."' width='100%' height='100px' class='thumbnail'></td>
	        										<td>".$row2['description']."</td>
	        										<td><a onclick='return handleClick();'href='my_contents.php?file=".$row2['download']."'>Download</a></td>
	        									</tr>
	        									<script>
              										function handleClick()
             											{alert('Pirataria é crime! Concordando com nossos termos de uso você se comprometeu a não repassá-lo a terceiros.');}
            									</script>
	        								";
	        							
	        							}
        							}

        						}
    							catch(PDOException $e){
									echo "Há algum problema na conexão: " . $e->getMessage();
								}

        						$pdo->close();
        					?>
        					</tbody>
        				</table>
	        		</div>
	        	</div>	        	
	        </div>
	    	</section>	     
		</div>
	</div>	        		
  	<?php include 'includes/footer.php'; ?>
  	<?php include 'includes/profile_modal.php'; ?>
</div>

<?php include 'includes/scripts.php'; ?>

</body>
</html>