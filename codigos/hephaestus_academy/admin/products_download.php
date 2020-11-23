<?php
	include 'includes/session.php';

	if(isset($_POST['upload'])){
		$id = $_POST['id'];
		$filename = $_FILES['download']['name'];

		$conn = $pdo->open();

		$stmt = $conn->prepare("SELECT * FROM products WHERE id=:id");
		$stmt->execute(['id'=>$id]);
		$row = $stmt->fetch();

		if(!empty($filename)){
			$ext = pathinfo($filename, PATHINFO_EXTENSION);
			$new_filename = $row['slug'].'_'.time().'.'.$ext;
			move_uploaded_file($_FILES['download']['tmp_name'], '../destination/'.$new_filename);	
		}
		
		try{
			$stmt = $conn->prepare("UPDATE products SET download=:download WHERE id=:id");
			$stmt->execute(['download'=>$new_filename, 'id'=>$id]);
			$_SESSION['success'] = 'Arquivo do conteúdo atualizado com sucesso';
		}
		catch(PDOException $e){
			$_SESSION['error'] = $e->getMessage();
		}

		$pdo->close();

	}
	else{
		$_SESSION['error'] = 'Primeiro selecione o conteúdo para atualizar o arquivo';
	}

	header('location: products.php');
?>