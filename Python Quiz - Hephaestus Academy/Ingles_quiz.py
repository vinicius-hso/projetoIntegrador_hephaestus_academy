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

q1 = ["Qual é a traducão para o verbo de ligacão 'To be'?",
      "Ser/estar", "Sentir", "Parecer", "Soar", 1]

q2 = ["Qual é a traducão para o verbo de ligacão 'To become'?",
      "Cheirar", "Tornar", "Escutar", "Comer", 2]

q3 = ["Qual é a traducão para o verbo de ligacão 'To feel'?",
      "Parecer", "Provar", "Sentir", "Soar", 3]

q4 = ["Qual é a traducão para o verbo de ligacão 'To smell'?",
      "Ser/estar", "Parecer", "Provar", "Cheirar", 4]

q5 = ["Qual é a traducão para o verbo de ligacão 'To taste'?",
      "Ficar", "Soar", "Parecer", "Provar", 4]

q6 = ["Qual a tradução para o adjetivo 'Adorável'?",
      "Adorable", "Agressive", "Stubborn", "Healthy", 1]

q7 = ["Qual a tradução para o adjetivo 'Amigável'?",
      "Funny", "Friendly", "Fearless", "Fair", 2]

q8 = ["Qual a tradução para o adjetivo 'Alegre'?",
      "Shy", "Sad", "Joyfull", "Modest", 3]

q9 = ["Qual a tradução para o adjetivo 'Ingênuo'?",
      "Thin", "Daring", "Wise", "Naive", 4]

q10 = ["Qual a tradução para o adjetivo 'Lindo'?",
       "Generous", "Honest", "Big", "Gorgeous", 4]

q11 = ["Qual a tradução para o adjetivo 'Loyal'?",
       "Leal", "Decidido", "Egoísta", "Engraçado", 1]

q12 = ["Qual a tradução para o adjetivo 'Angry'?",
       "Pobre", "Furioso", "Irritante", "Ousado", 2]

q13 = ["Qual a tradução para o adjetivo 'Mean'?",
       "Gordo", "Otimista", "Maldoso", "Rico", 3]

q14 = ["Qual a tradução para o adjetivo 'Usefull'?",
       "Talentoso", "Simpático", "Paciente", "Útil", 4]

q15 = ["Qual a tradução para o adjetivo 'Lucky'?",
       "Pesado", "Liberal", "Decidido", "Sortudo", 4]

q16 = ["Qual a tradução para o pronome indefinido 'Someone'?",
       "Alguém", "Ninguém", "Algum lugar", "Algo", 1]

q17 = ["Qual a tradução para o pronome indefinido 'Somebody'?",
       "Ninguém", "Alguém", "Nada", "Algo", 2]

q18 = ["Qual a tradução para o pronome indefinido 'Something'?",
       "Alguém", "Nada", "Algo", "Ninguém", 3]

q19 = ["Qual a tradução para o pronome indefinido 'Somewhere'?",
       "Qualquer lugar", "Ninguém", "Algum lugar", "Algo", 3]

q20 = ["Qual a tradução para o pronome indefinido 'No one'?",
       "Alguém", "Algum lugar", "Nada", "Ninguém", 4]

q21 = ["Qual o superlativo da palavra 'Grande'?",
       "The Biggest", "The Longest", "The Smallest", "The Youngest", 1]

q22 = ["Qual o superlativo da palavra 'Fofo'?",
       "The Newest", "The Cutest", "The Nicest", "The Tallest", 2]

q23 = ["Qual o superlativo da palavra 'Fácil'?",
       "The Strongest", "The Oldest", "The Easiest", "The Shortest", 3]

q24 = ["Qual o superlativo da palavra 'Difícil'?",
       "The Newest", "The Shortest", "The Nicest", "The Hardest", 4]

q25 = ["Qual o superlativo da palavra 'Forte'?",
       "The Youngest", "The Smallest", "The Shortest", "The Strongest", 4]

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
        screen.draw.filled_rect(box, "#012169")

    screen.draw.textbox(str(time_left), timer_box, color=("#C8102E"))
    screen.draw.textbox(question[0], main_box, color=("#C8102E"))

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
