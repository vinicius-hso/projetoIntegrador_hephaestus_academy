import pgzrun
import pygame
import random
pygame.init()
pygame.mixer.music.load('soundtrack.mp3')

pygame.mixer.music.play()
pygame.event.wait()

WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 30

q1 = ["O que é hardware?", "Talheres, parafusos e peças", "máquina de fresa e chave inglesa",
      "qualquer componente ou equipamento físico dentro e fora de um computador", "… o que você xinga!", 3]

q2 = ["Uma piada antiga em TI separa bem o hardware do software:", "Software é o que você xinga e hardware é o que você chuta",
      "Software é impossível existir sem o hardware", "Código fonte que faz o programa funcionar e servidor de internet",
      "Programas com erro e objetos de estimação de um programador", 1]

q3 = ["Quais os tipos de hardwares existentes?", "Padrão e externo", "Voláteis e não voláteis",
      "Ponte Sul e Ponte Norte", "Interno e Externo", 4]

q4 = ["O que é placa-mãe?", "Santa memória mãe do DOS", "Responsável pela interconexão de todos as peças que formam um pc",
      "… o cérebro de todo computador e celular", "Unidade Central de Processamento", 2]

q5 = ["Como são classificadas as placa-mãe?", "Mainboard e onboard", "Passiva e dissipadora",
      "Onboard e offboard", "Offboard e ATX", 3]

q6 = ["O que é CPU?", "O cérebro de todo computador e celular do planeta", "… o gabinete",
      "Mecanismo para dissipar calor", "Interface que integra o computador", 1]

q7 = ["O que são memórias?", " São formas complexas de prevenir demências", "Lembranças de tempos remotos",
      "dispositivos que podem armazenar informações", "Santa genitora mãe do DOS", 3]

q8 = ["Como são classificadas as memórias?", "Dinâmica e estática", "Voláteis e não voláteis",
      "Internas e externas", "Memória secundária e memória principal", 4]

q9 = ["Qual a característica da memória principal?", "Armazena dados temporariamente", "Acesso somente de leitura",
      "Mostra resultados da ação executada" , "transmite sons ao computador", 1]

q10 = ["Qual a característica da memória secundária?", "Lê caracteres digitados pelo usuário",
       "Lê os movimentos e toques dos botões","Armazena informações permanentemente", "Insere dados", 3]

q11 = ["Umas das funções da BIOS é:", "Salvar e ler dados essenciais", "Otimizar o processador",
       "Armazenar informação digital", "Verificar os dados de inicialização dos dispositivos", 4]

q12 = ["Os populares pen drives também são chamados de:", "Flash Drives", "Security Digital", "Solid State Drive", "One Drive", 1]

q13 = ["Qual do significado de RAM?", "Rate Action Memory", "Random Acess Memory", "Range Acess Memory", "Rule Active Memory", 2]

q14 = ["Sabendo que a memória RAM é parte essencial para o funcionamento do computador ela só pode ser:",
       "Expandida e contraída", "Transmissora de energia", "Gerenciadoras de dados", "Expandida ou removida", 4]

q15 = ["Qual a função dos dispositivos de entrada?", "Fazer inserção de corrente elétrica", "Gravar e ler dados",
       "Inserir informações na memória", "Realizar comunicação com o usuário", 3]

q16 = ["Qual a função dos dispositivos de saída?", "Mostrar o resultado da operação executada", "Ler dados de discos CD-ROM",
       "Auxiliar na refrigeração dos componentes", "Fornecer ar fresco para o cooler", 1]

q17 = ["Como é a composição básica de um Cooler?", "Bloco de estanho e cobre com uma ventoinha acoplada",
       "Bloco de prata ou plástico com uma ventoinha acoplada", "Bloco de metal ou níquel com uma ventoinha acoplada",
       "Bloco de alumínio ou cobre com uma ventoinha de cobre acoplada", 4]

q18 = ["Costumamos chamar essa velocidade do processador de:", "Crock", "Rock", "Morse", "Clock", 4]

q19 = ["Exemplo de memórias secundárias são:", "Memórias RAM e Memórias Cache",
       "Discos rígidos, cartões de memória, pendrives, HDs externos, etc.", "Memória ROM e Cartão SD",
       "POST e SSDs", "BIOS e Disco rígido", 2]

q20 = ["Quais os principais cooler para computador?", "Ativo, passivo, a ar e watercooler", "Passivo, a ar com Heat-pipe, watercooler",
       "Passivo, a ar, a ar com Heat-pipe, watercooler","Passivo, reflexivo, a gás, a ar", 3]

q21 = ["O que significa memória volátil?", "Dados inscritos nela se perdem quando não há energia a alimentando",
       "Alta velocidade de transferência de dados", "Velocidade mínima de transferência de dados", "Pode ser apagada e reescrita conforme necessário", 1]

q22 = ["A sigla HD significa?", "High Disk", "Hatch Disk", "Hard Disk", "Heap Disk", 3]

q23 = ["O chipset é um chip responsável pelo controle de uma série de itens da placa-mãe, é bastante comum que existam dois chips para esses controles:",
       "Ponte Sul e Ponte Norte", "Ponte Sul e ponte oeste", "Ponte cardinal e ordinal", "Ponte nordeste e ponte sudeste", 1]

q24 = ["Qual o papel fundamental da ventoinha no cooler?", "Filtrar e reter as impurezas externas", "Puxar ar quente para dentro do gabinete",
       "Manter o fluxo de ar constante para auxiliar a troca de calor", "Dispersar a energia gerada pelo processador", 3]

q25 = ["Quais componentes geram mais calor no computador?", "Chipset e memória RAM", "Placa-mãe e HD", "CPU e placas de vídeos", "Placas de vídeos e chipset", 2]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
             q11, q12, q13, q14, q15, q16, q17, q18, q19, q20,
             q21, q22, q23, q24, q25]

# gerando questões aleatórias
question = questions.pop(random.randrange(len(questions))) 

# pintando a tela
def draw():
    screen.fill("#F9F9F9")
    screen.draw.filled_rect(main_box, "#F9F9F9")
    screen.draw.filled_rect(timer_box, "#F9F9F9")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "#BECE9E")

    screen.draw.textbox(str(time_left), timer_box, color=("#C8102E"))
    screen.draw.textbox(question[0], main_box, color=("#000000"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("#F9F9F9"))
        index = index + 1

def game_over_happy():
    global question, time_left
    message = "Fim de jogo! Você acertou %s questões!" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def game_over():
    global question, time_left
    message = "Fim de jogo! Você acertou %s questões!" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0


def correct_answer():
    global question, score, time_left

    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 30
    else:
        print("Fim das questões")
        game_over_happy()
        pygame.mixer.music.load('happygameover.mp3')
        pygame.mixer.music.play()
        
def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicado na resposta " + str(index))
            if index == question[5]:
                print("Voce acertou!")
                correct_answer()
            else:
                game_over()
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
        index = index + 1

def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()
    
clock.schedule_interval(update_time_left, 1.0)

pgzrun.go()
