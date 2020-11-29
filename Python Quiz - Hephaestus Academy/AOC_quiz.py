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
time_left = 10

q1 = ["O que é Software?", "Conjunto de programas", "A memória de um PC",
      "Componentes físicos", "CPU", 1] 

q2 = ["Um byte é formado por quantos bits?", "2", "16", "8", "64", 3] 

q3 = ["Qual componente é considerado o cérebro de um computador?",
      "Placa mãe", "CPU", "UC", "ULA", 2] 

q4 = ["Dados são armazenados na forma:", "Analógica", "Decimal", "Octal",
      "Binário", 4] 

q5 = ["Qual a diferença entre Megabyte e Megabit?", "Megabit é maior",
      "São iguais", "Megabyte é maior", "O nome é diferente", 3] 

q6 = ["Qual é a memória principal?", "ROM", "RAM", "Cache", "Registrador", 2] 

q7 = ["Disco rígido é:", "Memória principal", "memória cache",
      "Memória Auxiliar", "Registrador", 3] 

q8 = ["CISC facilita o trabalho do:", "Programador", "Técnico",
      "Eletricista", "Usuário", 1] 

q9 = ["Qual desses é um tipo de placa mãe?", "BIOS", "ECC", "IDE", "ATX", 4] 

q10 = ["É uma unidade de entrada e de saída:", "Web Cam", "Scanner",
       "Pen Drive", "Plotters", 3] 

q11 = ["A ESD é especialmente perigosa para:", "o técnico",
       "os circuitos integrados", "o software", "os periféricos", 2] 

q12 = ["Qual a principal causa da ESD?", "A umidade", "Os condutores elétricos",
       "Os energéticos", "A eletricidade estática", 4] 

q13 = ["É um exemplo de material isolante:", "O plástico", "Os metais",
       "A água", "O silício", 1] 

q14 = ["É um tipo de ESD:", "O incêndio", "A explosão", "O raio", "A chuva", 3] 

q15 = ["A partir de que voltagem um dispositivo pode ser danificado", "20V",
       "12V", "300V", "5V", 2]  

q16 = ["Qual é o sistema de numeração que usamos no nosso dia a dia?",
       "Decimal", "Binário", "Octal", "Hexadecimal", 1] 

q17 = ["Qual é o sistema de numeração usado pelos computadores?", "Base 16",
       "Base 10", "Base 8", "Base 2", 4] 

q18 = ["Quantos bytes há em um terabyte?", "Mil", "Um milhão", "Um trilhão",
       "Um quatilhão", 3] 

q19 = ["A letra 'C' representa qual nº no sistema hexadecimal?", "10", "12", "14", "16", 2] 

q20 = ["Para representar um nº do sistema decimal, usamos a equação:", 'Moderada', 'De 1º grau', 'De 2º grau', 'Ponderada', 4] 

q21 = ["Qual é o maior?", "Yottabyte", "Zettabite", "Petabyte", "Exabite", 1]  

q22 = ["NÃO é um material adequado para se evitar a ESD:", "Caixa condutiva", "Cabo de aterramento", "Luvas de borracha", "Mamta antistática", 3] 

q23 = ["Qual tipo de material não permite a entrada de campos eletrostáticos?", "Condutores", "Condutivos", "Antiestáticos", "Isolantes", 2] 

q24 = ["NÃO é um tipo de memória:", "EPROM", "SSD", "SDRAM", "Bus", 4] 

q25 = ["Qual destes está no topo da hierarquia de memórias?", "Memória principal", "Memória auxiliar", "Registradores", "ROM", 3] 

q26 = ["Qual destes pode ser considerado um computador?", "Carro", "Rádio", "Ábaco", "Caderno", 3] 

q27 = ["Quando surgiu a primeira geração de computadores?", "Século 19", "Década de 1950", "Década de 1940", "Década de 1930", 2] 

q28 = ["O que marcou a 3ª geração de computadores?", "Circuito integrado", "Uso de válvulas", "Microcomputadores", "Transistores", 1] 

q29 = ["A rede de computadores surgiu em qual geração?", "3ª", "4ª", "5ª", "6ª", 2] 

q30 = ["Qual geração de computadores é a atual?", "3ª", "4ª", "5ª", "6ª", 3] 

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
             q11, q12, q13, q14, q15, q16, q17, q18, q19, q20,
             q21, q22, q23, q24, q25, q26, q27, q28, q29, q30]

# gerando questões aleatórias
question = questions.pop(random.randrange(len(questions))) 

# pintando a tela
def draw():
    screen.fill("#F9F9F9")
    screen.draw.filled_rect(main_box, "#F9F9F9")
    screen.draw.filled_rect(timer_box, "#F9F9F9")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "#808083")

    screen.draw.textbox(str(time_left), timer_box, color=("#5EAF3F"))
    screen.draw.textbox(question[0], main_box, color=("#5EAF3F"))

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
        time_left = 10
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
