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

q1 = ["No contexto de Algoritmos, o que são 'Instruções/Comandos'?",
"frases que indicam as ações a serem executadas", "escrita formal de códigos", "Modo de agir", "Modo de pensar", 1]

q2 = ["No contexto de Algoritmos, o que são 'Pseudocódigos'?",
"Do latim, significa código falso", "forma de representação de algoritmos", "Códigos em Python", "Segurança dos códigos", 2]

q3 = ["Qual alternativa é a Linguagem de Programação de mais alto nível?",
"C++", "Fortran", "Pseudocódigo", "Python", 4]

q4 = ["Qual comando para transformaruma variável em string em Python?",
"str()", "convert_string()", "int_to_str()", "string()", 1]

q5 = ["Qual comando para transformaruma variável em inteiro em Python?",
"inteiro()", "convert_int()", "int()", "integer()", 3]

q6 = ["Qual comando para transformar uma variável em decimal em Python?",
"dec()", "convert_dec()", "float()", "int_to_dec()", 3]

q7 = ["Qual comando para transformar verificar o tipo de uma variável em Python?",
"ty()", "type()", "ver_type()", "tipo()", 2]

q8 = ["Qual símbolo usado para atribuir valor em Python?",
":", "#", "=", "!", 3]

q9 = ["Qual símbolo usado para realizar uma comparação em Python?",
"=", "::", "==", "comp()", 3]

q10 = ["Qual a resposta de 'print(2/3)' em Python?",
"0.6666666666666666", "0.67", "0", "1", 1]

q11 = ["Qual a resposta de 'print(int(2/3))' em Python?",
"0.6666666666666666", "0.67", "0", "1", 3]

q12 = ["Qual símbolo usado para pular uma linha dentro de uma string em Python?",
"enter", "\n", "\p", "\jump", 2]

q13 = ["Qual o tipo da seguinte variável em Python 'var = [4, 1.2, 'python È legal]'?",
"integer", "dict", "bool", "list", 4]

q14 = ["Qual o tipo da seguinte variável em Python var = 'python É legal'?",
"string", "dict", "bool", "list", 1]

q15 = ["Qual o tipo da seguinte variável em Python 'var = 5'?",
"string", "dict", "int", "list", 3]

q16 = ["Qual o tipo da seguinte variável em Python 'var = 5.0'?",
"string", "float", "int", "list", 2]

q17 = ["Qual a saída: 'print(teste\\teste)'?",
"teste\\teste", "teste\teste", "invalid sintax", "nenhuma das alternativas", 2]

q18 = ["Qual o tipo da seguinte variável em Python 'True'?",
"bool", "float", "int", "list", 1]

q19 = ["Qual o tipo da seguinte variável em Python 'var = {}'?",
"string", "null", "dict", "list", 3]

q20 = ["Qual o tipo da seguinte variável em Python 'var = []'?",
"string", "float", "null", "list", 4]

q21 = ["Qual o operador para exponenciação em Python?",
"exponential()", "expo()", "**", "^", 3]

q22 = ["Qual o operador para Multiplicação em Python?",
"exponential()", "expo()", "*", "^", 3]

q23 = ["Qual o operador utilizado para obter o resto de uma divisão em Python?",
"//", "%", "/", "resto()", 2]

q24 = ["Qual a resposta de 'print(2//3)' em Python?",
"0.6666666666666666", "0.67", "0", "1", 3]

q25 = ["Qual das alternativas representa o comando para estabelecer uma relação condicional em Python?",
"se", "and", "or", "if", 4]

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
        screen.draw.filled_rect(box, "#FBE59B")

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
