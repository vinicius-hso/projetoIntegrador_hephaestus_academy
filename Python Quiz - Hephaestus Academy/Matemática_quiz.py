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

q1 = ['Em matemática discreta a que refere-se a seguinte definição "esquemas simplificados com pontos e linhas ligando-os sob certas condições?"',
"Inequações", "Equações", "Grafos", "Geometria", 3]

q2 = ["Em matemática discreta as pontes de Königsberg compõem qual cotexto?",
"Inequações", "Equações", "Grafos", "Geometria", 3]

q3 = ["Considerando V = {X, Y, Z, W} e A = {{X, Y}, {X, Z}, {X, W}, {Y, Z}, {Z, W}}, temos que G1 = (V, A). Há quantos vértices?",
"8", "4", "5", "25", 2]

q4 = ["Considerando V = {X, Y, Z, W} e A = {{X, Y}, {X, Z}, {X, W}, {Y, Z}, {Z, W}}, temos que G1 = (V, A). Há quantas arestas?",
"8", "4", "5", "25", 3]

q5 = ["Qual o complemento do Grafo G4, sendo que G4 = (V, A), V = {1, 2, 3, 4, 5} e A = {{1, 2}, {1, 4}, {2, 3}, {2, 5}, {3, 4}, {4, 5}}?",
"G'4 = {{1, 3}, {1, 8}, {2, 4}, {3, 8}}", "G'4 = {{2, 3}, {1, 5}, {2, 3}, {3, 5}}", "G'4 = {{1, 3}, {1, 5}, {2, 4}, {3, 5}}", "G'4 = {{1, 3}, {1, 5}, {2, 9}, {8, 5}}", 3]

q6 = ["O que é o grau do vértice?",
"quantidade de elementos de vizG(x)", "elevação do grafo G(x)", "exponenciação de G(x)", "número de vértices de um grafo", 1]

q7 = ["Sabendo que o grafo possui n vértices, qual o valor do grau dos vértices para que um grafo seja completo?",
"0", "1", "n", "n-1", 4]

q8 = ["Qual é o valor do grau de um vértice de um grafo, para que ele seja considerado isolado?",
"0", "1", "n", "n-1", 1]

q9 = ["Qual é o valor do grau de um vértice de um grafo, para que ele seja considerado folha?",
"0", "1", "n", "n-1", 2]

q10 = ["Se um grafo tem n vértices, qual seu número máximo de arestas?",
"0", "1", "n(n - 1)/2", "n-1", 3]



questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

# gerando questões aleatórias
question = questions.pop(random.randrange(len(questions))) 

# pintando a tela
def draw():
    screen.fill("#F9F9F9")
    screen.draw.filled_rect(main_box, "#F9F9F9")
    screen.draw.filled_rect(timer_box, "#F9F9F9")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "#F5B169")

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
