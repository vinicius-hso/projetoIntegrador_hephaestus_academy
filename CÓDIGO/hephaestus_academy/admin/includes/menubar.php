<aside class="main-sidebar">
  <!-- sidebar: style can be found in sidebar.less -->
  <section class="sidebar">
    <!-- Sidebar user panel -->
    <div class="user-panel">
      <div class="pull-left image">
        <img src="<?php echo (!empty($admin['photo'])) ? '../images/'.$admin['photo'] : '../images/profile.jpg'; ?>" class="img-circle" alt="User Image">
      </div>
      <div class="color_white pull-left info">
        <p><?php echo $admin['firstname'].' '.$admin['lastname']; ?></p>
        <a class='color_white'><i class="fa fa-circle text-success"></i> Online</a>
      </div>
    </div>
    <!-- sidebar menu: : style can be found in sidebar.less -->
    <ul class="sidebar-menu" data-widget="tree">
      <li class="header">RELATÓRIO</li>
      <li><a class='color_white' href="home.php"><i class="fa fa-dashboard"></i> <span>Relatórios</span></a></li>
      <li><a class='color_white' href="sales.php"><i class="fa fa-money"></i> <span>Vendas</span></a></li>
      <li class="header">GERENCIAMENTO</li>
      <li><a class='color_white' href="users.php"><i class="fa fa-users"></i> <span>Usuários Cadastrados</span></a></li>
      <li class="treeview">
        <a class='color_white' href="#">
          <i class="fa fa-barcode"></i>
          <span>Conteúdos Didáticos</span>
          <span class="pull-right-container">
            <i class="fa fa-angle-left pull-right"></i>
          </span>
        </a>
        <ul class="treeview-menu">
          <li><a class='color_white' href="products.php"><i class="fa fa-circle-o"></i> Lista de Conteúdos</a></li>
          <li><a class='color_white' href="category.php"><i class="fa fa-circle-o"></i> Lista de Categorias</a></li>
        </ul>
      </li>
    </ul>
  </section>
  <!-- /.sidebar -->
</aside>