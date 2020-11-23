<?php
	include 'includes/session.php';
	include 'includes/slugify.php';

	if(isset($_POST['add'])){
		$name = $_POST['name'];
		$slug = slugify($name);
		$category = $_POST['category'];
		$price = $_POST['price'];
		$description = $_POST['description'];
		$filename = $_FILES['photo']['name'];
		$filename2 = $_FILES['download']['name'];

		$conn = $pdo->open();

		$stmt = $conn->prepare("SELECT *, COUNT(*) AS numrows FROM products WHERE slug=:slug");
		$stmt->execute(['slug'=>$slug]);
		$row = $stmt->fetch();

		if($row['numrows'] > 0){
			$_SESSION['error'] = 'Item já existe';
		}
		else{
			if(!empty($filename)){
				$ext = pathinfo($filename, PATHINFO_EXTENSION);
				$new_filename = $slug.'.'.$ext;
				move_uploaded_file($_FILES['photo']['tmp_name'], '../images/'.$new_filename);	
			}
			if(!empty($filename2)){
				$ext2 = pathinfo($filename2, PATHINFO_EXTENSION);
				$new_filename2 = $slug.'_file.'.$ext2;
				move_uploaded_file($_FILES['download']['tmp_name'], '../destination/'.$new_filename2);	
			}
			else{
				$new_filename = '';
				$new_filename2 = '';
			}

			try{
				$stmt = $conn->prepare("INSERT INTO products (category_id, name, description, slug, price, photo, download) VALUES (:category, :name, :description, :slug, :price, :photo, :download)");
				$stmt->execute(['category'=>$category, 'name'=>$name, 'description'=>$description, 'slug'=>$slug, 'price'=>$price, 'photo'=>$new_filename, 'download'=>$new_filename2]);
				$_SESSION['success'] = 'Conteúdo adicionado com sucesso';

			}
			catch(PDOException $e){
				$_SESSION['error'] = $e->getMessage();
			}
		}

		$pdo->close();
	}
	else{
		$_SESSION['error'] = 'Primeiro preencha o formulário de cadastro de conteúdo';
	}

	header('location: products.php');

?>