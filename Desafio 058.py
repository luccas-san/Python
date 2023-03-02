from time import sleep
from random import randint
sorte = randint(0, 10)
print('Estou pensando em um número de 0 a 10.')
sleep(1)
print('Consegue advinhar qual é?')
option = str(input('Sim ou Não? [S/N]: ')).strip().upper()
if option in 'Ss':
    print('Vamos começar. Vou te dando algumas dicas ao longo do jogo.')
elif option in 'Nn':
    print('Tente algumas vezes. Garanto que não é dificil.')
    sleep(1)
    print('Eu te ajudo com algumas dicas para facilitar...')
    sleep(1.25)
cont = 0
acertou = False
sleep(1)
while not acertou:
    sleep(0.5)
    jogador = int(input('Qual é o seu palpite? Digita ai: '))
    cont = cont + 1
    if jogador == sorte:
        acertou = True
        print('Parabéns!!! Você acertou')
        print(f'Eu pensei no número {sorte}')
        if option in 'Nn':
            print('Eu sabia que não era dificil pra você.')
    if jogador < sorte:
        print('Mais... Tente mais uma vez.')
    if jogador > sorte:
        print('Menos... Tente mais uma vez.')
print(f'Você acertou depois de {cont} tentativa(s)')
#Outro Modo
#from random import randint
#computador = randint (0, 10)
#print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
#print('Será que você consegue adivinhar qual foi?')
#acertou = false
#palpites = 0
#while not acertou:
#   jogador = int(input('Qual é o seu palpite?))
#   palpites += 1
#   if jogador == computador:
#   acertou = true
#   else:
#   if jogador < computador:
#       print('Mais... Tente mais uma vez.')
#   elif jogador > computador:
#       print('Menos... Tente mais uma vez.')
#print('Acertou com {} tentativas. Parabens!'.format(palpites))