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

q1 = ["Assinale a opção correta.", 
"Há de ser corrigidos os erros", "Hão de ser corrigidos os erros", "Hão de serem corrigidos os erros", "Há de ser corrigidos os erros", 2]

q2 = ["Assinale a alternativa que completa corretamente as lacunas: _____ profissionais mais competentes, se existissem melhores condições de ensino.",
"Deveriam haver", "Deveria haver", "Deveriam haverem", "Deveríamos haver", 2]

q3 = ["Não há erro de concordância nesta alternativa:",
"Alugam-se apartamentos", "Alugam-se apartamento", "Alugase apartamentos", "n.d.a", 1]

q4 = ["Complete a frase: Ora, _____ meses que não _____ na escola fatos como aquele que até agora nos perturbam.",
"faz, ocorrem", "fazem, ocorre", "faz, ocorre", "n.d.a", 1]

q5 = ["Marque a alternativa em que a concordância contraria a norma culta.",
"Ouviram‑se as notícias mais desencontradas", "Trata‑se de questões muito sérias", "Faziam anos que o país não escolhia o presidente", "n.d.a", 3]

q6 = ["Assinale a alternativa correta quanto à concordância verbal.",
"Iam dar seis horas no relógio da praça", "Iam-se dar seis horas no relógio da praça", "Ia da seis horas no relógio da praça", "n.d.a", 1]

q7 = ["Assinale a alternativa correta quanto à concordância verbal.",
"Somos nós quem paga a conta pelo descaso", "Somo nós que paga a conta pelo descaso", "Samos nós quem pagam a conta pelo descaso", "n.d.a", 1]

q8 = ["Assinale a opção correta.",
"A maioria dos conflitos foram resolvidos", "As maioria do conflitos foram resolvidos", "A maiorias do conflitos fora resolvidos", "n.d.a", 1]

q9 = ["Assinale a opção correta.",
"Devem haver bons motivos para a sua recusa", "Deve haver bons motivos para a sua recusa", "Deve haverem bons motivos para a sua recusa", "n.d.a", 2]

q10 = ["Assinale a alternativa correta quanto à concordância verbal.",
"De casa à escola é três quilômetros", "De casa à escola são três quilômetros", "De casa à escola sãos três quilômetro", "n.d.a", 2]

q11 = ["Não há erro de concordância nesta alternativa:",
"Nem uma nem outras questão é difícil", "Nem uma nem outra questões é difícil", "Nem uma nem outra questão é difícil", "n.d.a", 3]

q12 = ["Assinale a alternativa correta quanto à concordância verbal.",
"Pintaram-se as paredes de verde", "Pintou-se as paredes de verde", "Pintaram as paredes de verde", "n.d.a", 1]

q13 = ["Assinale a opção correta.",
"Organizou-se em grupos de quatro", "Organizou-ses em grupos de quatro", "Organizou-se em grupo de quatros", "n.d.a", 1]

q14 = ["Não há erro de concordância nesta alternativa:",
"Já faz mais de dez anos que o vi", "Já fazem mais de dez anos que o vi", "Já fazem-se mais de dez anos que o vi", "n.d.a", 1]

q15 = ["Complete a frase: Água às refeições é _____ para a saúde.",
"Mau", "Má", "Mal", "n.d.a", 1]

q16 = ["Observe a concordância, qual alternativa está incorreta?",
"Entrada proibida", "É proibido entrada", "Para quem a entrada é proibido?", "n.d.a", 3]

q17 = ["Complete a frase: Cabelo e pupila _____.",
"Negro", "Negros", "Negras", "Negra", 2]

q18 = ["Preencha a lacuna: Seguem _____ às cartas minhas poesias para você.",
"Anexa", "Anexas", "Anexo", "Anexos", 2]

q19 = ["Complete a frase: Polvo e lula _____ serão servidos no jantar.",
"Frescos", "Fresco", "Frescas", "Fresca", 4]

q20 = ["Preencha a lacuna: Para a matrícula, é _____ a documentação pedida.",
"Necessário", "Necessários", "Necessária", "Necessárias", 3]

q21 = ["Qual é a frase correta?",
"Ela está meia nervosa", "Ela estás meia nervosa", "Ela está meio nervosa", "n.d.a", 3]

q22 = ["Assinale a opção em que a concordância nominal contraria a norma culta da língua:",
"Uso louça e copo velhos", "Uso copo e louça velhas", "Uso copo e louça velhos", "n.d.a", 2]

q23 = ["Marque a frase inaceitável, do ponto de vista da concordância nominal:",
"É necessária paciência", "É bom bebermos cerveja", "É bom bebermos vinho", "n.d.a", 1]

q24 = ["Assinale a alternativa em que 'meio' funciona como advérbio.",
"Fica no meio do quarto", "Está meio triste", "Quero meio quilo", "n.d.a", 2]

q25 = ["Segundo a norma culta, a frase que está gramaticalmente correta é:",
"É proibido nadar neste local", "É proibida nadar neste local", "É proibido-se nadar neste local", "n.d.a", 1]

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
