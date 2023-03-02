import random
from time import sleep
print('-=-' * 20)
nome = str(input('Informe o seu Nome: ')).strip().capitalize()
print('-=-' * 20)
num = int(input('{} tente advinhar o Número entre 0 e 5 que estou pensando: '.format(nome)))
print('Deixa eu ver qual Número foi...')
sleep(2)
print('Você escolheu o número {}'.format(num))
print('PROCESSANDO...')
sorteio = random.randint(0,5)
sleep(3)
print('O número que eu pensei foi: {}'.format(sorteio))
if sorteio == num:
    print('Parabens, {}. Você acertou o número sorteado.'.format(nome))
else:
    print('Sinto muito, {}. Você errou. Eu venci essa!'.format(nome))
sleep(3)
print('Quer Tentar outra vez?')
