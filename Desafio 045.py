from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua Jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 20)
print('Computador Jogou {}'.format(itens[computador]))
print('Jogador Jogou {}'.format(itens[jogador]))
print('-=-' * 20)
if computador == 0: #Computador Jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('Jogada Invalida!')
elif computador == 1: #Computador Jogou PAPEL
    if jogador == 0:
        print('Computador Venceu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador Venceu')
    else:
        print('Jogada Invalida')
elif computador == 2: #Computador Jogou TESOURA
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Invalida')
