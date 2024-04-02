import time
import pygame

def sound():
    som = "C:/Users/Edu/Documents/GitHub/cronometro/cronometro/soundcronometro.mp3"
    pygame.init()
    pygame.mixer.music.load(som)
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
    

def contagem(min, seg):
    contagem_total = int(min * 60 + seg)
    #Ficará dentro do loop do while até o momento do argumento passado na contagem, retornar o valor 0. (no caso valor 0 é um booleano False)
    while contagem_total > 0:
        min, seg = divmod(contagem_total, 60)
        #divmode é responsável por fazer uma divisão entre os dois números e separar o quociente do resto da divisão.
        #Podendo assim trabalhar com minutos e segundos corretamente.
        
        timer = (f"{min:02d}:{seg:02d}")
        #Estamos formatando o número inteiro pois queremos somente os dois primeiros números digitados pelo usuários
        #da esquerda para a direita. O resultado serão atribuidos dentro das variáveis min e seg. 

        print (timer, end="\r")
        time.sleep(1)
        #time.sleep é uma função pausa a execução durante um determinado tempo. Irá rodar essa função e aguardar 1 segundo neste caso.
        contagem_total -= 1
        

    print ("Me contrata por favor :)")
    #Lembrando que o print deve ficar fora do while.

minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

contagem (minutos, segundos)
sound()
