-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 07-Nov-2020 às 15:44
-- Versão do servidor: 10.4.14-MariaDB
-- versão do PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `ecomm`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE IF NOT EXISTS `cart` (
`id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE IF NOT EXISTS `category` (
`id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `cat_slug` varchar(150) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Data for table `category`
--

INSERT INTO `category` (`id`, `name`, `cat_slug`) VALUES
(1, 'Arquitetura e Organização de Computadores', 'arc_org_comp'),
(2, 'Hardware', 'hardware_'),
(3, 'Inglês', 'ingles_'),
(4, 'Lógica de Programação', 'log_prog'),
(5, 'Matemática Discreta', 'mat_disc'),
(6, 'Português', 'portugues');

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE IF NOT EXISTS `details` (
`id` int(11) NOT NULL,
  `sales_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

--
-- Data for table `details`
--

INSERT INTO `details` (`id`, `sales_id`, `product_id`, `quantity`) VALUES
(1, 9, 11, 1),
(2, 9, 12, 1),
(3, 9, 3, 1),
(4, 9, 1, 1),
(5, 10, 13, 1),
(6, 10, 2, 1),
(8, 11, 1, 1),
(9, 11, 2, 1),
(10, 11, 3, 1),
(11, 11, 4, 1),
(12, 11, 5, 1),
(13, 11, 6, 1),
(14, 11, 7, 1),
(15, 11, 8, 1),
(16, 11, 9, 1),
(17, 11, 10, 1),
(18, 11, 11, 1),
(19, 11, 12, 1),
(20, 11, 13, 1);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE IF NOT EXISTS `products` (
`id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text NOT NULL,
  `slug` varchar(200) NOT NULL,
  `price` double NOT NULL,
  `photo` varchar(200) NOT NULL,
  `date_view` date NOT NULL,
  `counter` int(11) NOT NULL,
  `download` varchar(200) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

--
-- data for table `products`
--

INSERT INTO `products` (`id`, `category_id`, `name`, `description`, `slug`, `price`, `photo`, `date_view`, `counter`, `download`) VALUES
(1, 5, 'Lógica Formal', '<p>Lógica Formal é definida como a ciência das leis do pensamento e a arte de aplicá-los corretamente na procura e demonstração da verdade. Seu objetivo é apresentar a diferença entre dedução e indução, as regras da dedução, sob a forma de silogismos e de argumentos condicionais, bem como os vários tipos de falácia. São objetos de estudo dessa unidade elaborada no formato de texto o seguintes temas: Proposição e Conectivos; Operações Lógicas Sobre Proposições; Construção de Tabelas-Verdade; Tautologias, Contradições e Contingências; Implicação e Equivalência Lógica; Método de Refutação Por Redução ao Absurdo; Exercícios de fixação como conteúdo complementar juntamente com gabarito.</p>\r\n', 'matematica-1', 10, 'logica_formal.jpg', '2020-11-03', 1000, '01_Lógica Formal - Hephaestus Academy.pdf'),
(2, 5, 'Introdução à Grafos', '<p>A Teoria do Grafos ou de Grafos é um ramo da matemática que estuda a relação entre os objetos de um determinado conjunto. Para tal são empregadas estruturas chamadas de gratos, G (V, E), onde V é um conjunto não vazio de objetos denominados vértices (ou nós) e E (do inglês edges - arestas) é um subconjunto de pares não ordenados de V. São objetos de estudo dessa unidade elaborada no formato de texto os seguintes temas: A Teoria dos Grafos; Grafos e Seus Principais Elementos;  Caminhos e Conexidade; Aplicação da Teoria dos Grafos; Exercícios de fixação como conteúdo complementar juntamente com gabarito.</p>\r\n', 'matematica-2', 10, 'grafos.jpg', '2020-11-03', 1000, '02_Introdução à Grafos - Hephaestus Academy.pdf'),
(3, 4, 'Instalando o Python', '<p>Através deste conteúdo você será capaz de instalar o Python em seu computador, livre de erros, pois é apresentado um passo a passo de todo o processo. Para melhor iteração e entendimento, este conteúdo está disponibilizado em formato vídeo</p>\r\n', 'logica-1', 10, 'python.jpg', '2020-11-03', 1000, '03_LEIA-ME_Instalando_Python_VIDEO.txt'),
(4, 4, 'Introdução à Implementação de Algoritmos', '<p>Este conteúdo em formato "Texto" aborda inicialmente uma introdução sobre algoritmos, bem como sua implementação utilizando como linguagem de apoio o Phyton. Serão discutidos os seqguintes temas: tipos de variáveis, operadores lógicos e aritméticos, relações condicionais e Iterações. Esses temas são fundamentais para quem está iniciando na programação.</p>\r\n', 'logica-2', 10, 'python_2.jpg', '2020-11-03', 1000, '04_Algoritmos e Lógica de Programação - Hephaestus Academy.pdf'),
(5, 4, 'Reconhecimento de Voz - I.A. em Python', '<p>Já ouviu falar sobre a Alexa da Amazon? Pois é. Neste conteúdo em formato "Vídeo" serão apresentados os fundamentos da implementação de Inteligência Artificial em Python. Após concluir esse conteúdo você será capaz de implementar um código que reconhece sua fala e responde na tela. Recomendamos que estude também os nossos conteúdos "Introdução a Implementação de Algoritmos" e "Instalando o Python", para um melhor aproveitamento deste conteúdo.</p>\r\n', 'logica-3', 10, 'robo.jpg', '2020-11-03', 1000, '05_LEIA-ME_Reconhecimento_Voz_Python_VIDEO.txt'),
(6, 6, 'Concordância', '<p>A Concordância Verbal e Nominal está estritamente ligada a forma correta de escrever e se comunicar. A boa escrita e uma boa comunicação são instrumentos indispensáveis no cotidiano de qualquer profissional, especialmente para aqueles que almejam um determinado crescimento profissional e pessoal. Portanto, não perca essa chance! Alcance seus objetivos investindo no seu futuro!</p>\r\n', 'port-1', 10, 'Concordancia01.png', '2020-11-03', 1000, '06_Concordância - Hephaestus Academy.pdf'),
(7, 6, 'Pontuação', '<p>A Pontuação na linguagem funciona como uma espécie de sinalização, guiando e organizando o texto a ser lido. Como em um trânsito, os sinais apontam onde deve haver pausas ou o que chama a atenção.  Se, mesmo com toda a sinalização, o trânsito nas cidades já é complicado, imagine sem! Assim como no tráfego de veículos, no texto os sinais dão ritmo, fluidez e evitam confusão. Por isso, a pontuação é superimportante. O texto mal pontuado se torna ininteligível. E não é isso que você deseja, não é mesmo?! Então, adquira nosso material exclusivo sobre Pontuação e se destaque!</p>\r\n', 'port-2', 10, 'Pontuacao01.png', '2020-11-03', 1000, '07_Pontuação - Hephaestus Academy.rar'),
(8, 1, 'Introdução à Arquitetura de Computadores','Este conteúdo em formato "Texto & Vídeo" aborda os seguintes temas: Conceito de Hardware e Software; Arquiteturas de Von Neumann e Harvard; Barramentos; Dispositivos E/S, CPU e Seus Componentes; Tipos de Memórias; Microprocessadores; Exercícios para praticar.</p>\r\n', 'computadores-1', 10, 'aoc1.jpg', '2020-11-03', 1000, '08_AOC Introdução CPU Memórias Microprocessadores - Hephaestus Academy.rar'),
(9, 5, 'Introdução à Lógica', '<p>Nesse conteúdo em formato de vídeo são apresentados os conceitos fundamentais da lógica e suas variações, assim como a Definição de Lógica; Origem da Lógica; Lógica Clássica e Anticlássica e suas subdivisões; Lógica Informal; Conceito de Argumento; Validade de Um Argumento; Argumentos Dedutivos e Indutivos; Verdade e Falsidade; Validade ou Invalidade; Questão de Raciocínio Lógico.</p>\r\n', 'matematica-3', 10, 'math_video.jpg', '2020-11-03', 1000, '09_LEIA-ME_Matemática-Lógica_VIDEO.txt'),
(10, 1, 'Sistemas Numéricos', '<p>Este conteúdo em formato "Texto" aborda os seguintes temas: Quantidades em Computação; Sistemas Numéricos; Valor Absoluto e Relativo; Equação Ponderada de Número Binário; Conversões de Base; Aplicação; Exercícios para praticar.</p>\r\n', 'computadores-4', 10, 'aoc4.jpg', '2020-11-03', 1000, '10_AOC - Sistemas de Numeração - Hephaestus Academy.rar'),
(11, 1, 'ESD', '<p>Este conteúdo em formato "Texto" aborda os seguintes temas: Causas da ESD; Indução Eletrostática; Tipos de ESD; Como Evitar ESD; Exercícios para praticar.</p>\r\n', 'computadores-5', 10, 'aoc5.jpg', '2020-11-03', 1000, '11_AOC - ESD e descargas elétricas - Hephaestus Academy.rar'),
(12, 2, 'Introdução à Hardware', '<p>Este conteúdo em formato "Texto & Vídeo" aborda os seguintes temas: O que é Hardware; Placa-Mãe; CPU; Processador; Memórias; Dispositivos de Armazenamento; Memória RAM; Dispositivos de Entrada e Saída; Sistemas de Refrigeração.</p>\r\n', 'hardware_02', 10, 'hardware01.jpg', '2020-11-03', 1000, '12_Hardware.rar'),
(13, 3, 'Inglês', '<p>Este conteúdo em formato "Texto" aborda os seguintes temas: Adjetivos; Principais Verbos de Ligação; Pronomes Indefinidos; Adjetivos Possessivos; Exercícios para praticar.</p>\r\n', 'ingles', 10, 'ingles.jpg', '2020-11-03', 1000, '13_Introdução Língua Inglesa - Hephaestus Academy.pdf');


-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE IF NOT EXISTS `sales` (
`id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `pay_id` varchar(50) NOT NULL,
  `sales_date` date NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- data for table `sales`
--

INSERT INTO `sales` (`id`, `user_id`, `pay_id`, `sales_date`) VALUES
(9, 2, 'PAY-1RT494832H294925RLLZ7TZA', '2020-11-11'),
(10, 2, 'PAY-21700797GV667562HLLZ7ZVY', '2020-11-11'),
(11, 3, 'PAY-51700797GV667562HLLZ7ZVY', '2020-02-11');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
`id` int(11) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` varchar(60) NOT NULL,
  `type` int(1) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `address` text NOT NULL,
  `contact_info` varchar(100) NOT NULL,
  `photo` varchar(200) NOT NULL,
  `status` int(1) NOT NULL,
  `activate_code` varchar(15) NOT NULL,
  `reset_code` varchar(15) NOT NULL,
  `created_on` date NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `type`, `firstname`, `lastname`, `address`, `contact_info`, `photo`, `status`, `activate_code`, `reset_code`, `created_on`) VALUES
(1, 'admin@admin.com', '$2y$10$0SHFfoWzz8WZpdu9Qw//E.tWamILbiNCX7bqhy3od0gvK5.kSJ8N2', 1, 'Antonio', 'Egydio', '', '', 'egydio.jpg', 1, '', '', '2020-07-06'),
(2, 'fmasanori@fatec.com', '$2y$10$TT5RPSGDiEP29vyMvo3rv.wMl332lNjJqbZwdnmtV4jlSELWreyl6', 0, 'Fernando', 'Masanori', 'Avenida Cesare Monsueto Giulio Lattes, 1350 Distrito', '55129999999', 'masanori.jpg', 1, 'k8FBpynQfqsv', 'wzPGkX5IODlTYHg', '2020-11-03'),
(3, 'jean@fatec.com', '$2y$10$Oongyx.Rv0Y/vbHGOxywl.qf18bXFiZOcEaI4ZpRRLzFNGKAhObSC', 0, 'Jean', 'Costa', 'Avenida Cesare Monsueto Giulio Lattes, 1350 Distrito', '55129999999', 'jean.jpg', 1, '', '', '2020-11-03');

--
-- Indexes for tables
--

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `details`
--
ALTER TABLE `details`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `details`
--
ALTER TABLE `details`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=30;
--
-- AUTO_INCREMENT for table `sales`
--
ALTER TABLE `sales`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=13;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
