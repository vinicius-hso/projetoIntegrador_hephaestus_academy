<header>
  <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark ">
    <a class="brand" href="index.php"><img class="logo_00" src=images/logo.png> Hephaestus Academy</a>

    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault"
      aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarsExampleDefault">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="category.php" id="dropdown01" data-toggle="dropdown"
            aria-haspopup="true" aria-expanded="false">Conteúdos</a>
            <ul class="dropdown-menu" role="menu">
              <?php
             
                $conn = $pdo->open();
                try{
                  $stmt = $conn->prepare("SELECT * FROM category");
                  $stmt->execute();
                  foreach($stmt as $row){
                    echo "
                      <li><a class='dropdown-item' href='category.php?category=".$row['cat_slug']."'>".$row['name']."</a></li>
                    ";                  
                  }
                }
                catch(PDOException $e){
                  echo "There is some problem in connection: " . $e->getMessage();
                }

                $pdo->close();

              ?>
            </ul>
          
        </li>
        <form method="POST" class="form-inline my-2 my-lg-0" action="search.php">
          <input class="caps " id="navbar-search-input" type="text" placeholder="Pesquisa" name="keyword" aria-label="Pesquisa">
            <button method="POST" type="submit" class="btn btn_srch">
              <svg action="search.php" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="btn_srch" role="img"
                viewBox="0 0 24 24" focusable="false">
                <title>Search</title>
                <circle cx="10.5" cy="10.5" r="7.5" />
                <path d="M21 21l-5.2-5.2" />
            </svg>
          </button>
        </form>
      </ul>

      <!-- Navbar Right Menu -->
      <div class="navbar-right">
        <ul class="navbar-nav">
          <li class="dropdown messages-menu">
            <!-- Menu toggle button -->
            <a href="#" class="dropdown-toggle" data-toggle="dropdown"> 
              <i class="nav-item dropdown"></i>
            </a>
            <ul class="dropdown-menu">              
              <li class="header">Você tem <span class="cart_count"></span> item(s) no carrinho</li>
              <li>
                <ul class="menu" id="cart_menu">
                </ul>
              </li>
              <li class="footer"><a href="cart_view.php">Vá para o carrinho</a></li>
            </ul>
            <span class="label label-success cart_count"></span>
            <a href="cart_view.php"><img class="btn_header2 logo_00" src=images/carrinho.png></a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="dropdown01" data-toggle="dropdown"
              aria-haspopup="true" aria-expanded="false">Pt <img class="flag_lang" src="images/pt.png"></a>
            <div class="dropdown-menu" aria-labelledby="dropdown01">
              <a class="dropdown-item" href="#">En <img class="flag_lang" src=images/en.png></a>
            </div>
          </li>


          <?php
            if(isset($_SESSION['user'])){
              $image = (!empty($user['photo'])) ? 'images/'.$user['photo'] : 'images/profile.jpg';
              echo '
                <li class="dropdown user user-menu">





                  <a href="#" class="nav-link dropdown-toggle dropdown-menu-right" data-toggle="dropdown">
                    <img src="'.$image.'" class="user-image" alt="User Image">
                    <span class="hidden-xs">'.$user['firstname'].' '.$user['lastname'].'</span>
                  </a>
                  <ul class="dropdown-menu dropdown-menu-right">
                    <!-- User image -->
                    <li class="user-header">
                      <img src="'.$image.'" class="img-circle" alt="User Image">

                      <p class="text-black bold_big">
                        '.$user['firstname'].' '.$user['lastname'].'
                      </p>
                    </li>
                    <li class="user-footer margim-more">
                      <div class="btn_user_div">
                        <a href="profile.php" class="btn_user btn-outline-success btn">Meus dados</a>
                      </div>
                      <div class="btn_user_div">
                        <a href="my_contents.php" class="btn_user btn-outline-success btn">Meus conteúdos</a>
                      </div>                      
                      <div class="btn_user_div">
                        <a href="logout.php" class="btn_user btn-success btn">Sair</a>
                      </div>
                    </li>
                  </ul>
                </li>
              ';
            }
            else{
              echo "
                <li><a class='btn_header btn btn-outline-success my-2 my-sm-0' href='login.php'>Login</a></li>
                <li><a class='btn_header btn btn-success my-2 my-sm-0' href='signup.php'>Registre-se</a></li>
              ";
            }
          ?>
        </ul>
      </div>
    </div>
  </nav>      
</header>