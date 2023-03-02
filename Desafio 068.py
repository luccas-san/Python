from time import sleep
from random import randint
sleep(0.5)
print('\033[1;32mIniciando...\033[m')
sleep(1)
print('\033[1;32m°°°\033[m\033[1;31m°°°\033[m' * 15)
print('Vamos jogar \033[1;32mPAR\033[m ou \033[1;31mIMPAR\033[m')
print('\033[1;32m***\033[m\033[1;31m***\033[m' * 15)
sleep(0.5)
win = 0
while True:
    num = int(input('Escolha um número: '))
    op = str(input('PAR ou IMPAR? [P/I]: ')).strip().upper()
    while op not in 'PI':
        op = str(input('PAR ou IMPAR? [P/I]: ')).strip().upper()
    computador = randint(1, 10)
    soma = num + computador
    par = 'Pp' and soma % 2 == 0
    impar = 'Ii' and soma % 2 == 1
    print(f'Você escolheu {num} e o computador {computador}. A soma é {soma}.',end=' ')
    if soma % 2 == 0 and op in 'Pp':
        print('Deu PAR!')
        print('Você \033[1;32mVENCEU\033[m!!! Vamos novamente...')
        print('\033[1;34m+++++\033[m' * 20)
        win += 1
    if soma % 2 == 1 and op in 'Ii':
        print('Deu IMPAR!')
        print('Você \033[1;32mVENCEU\033[m!!! Vamos novamente...')
        print('\033[1;34m+++++\033[m' * 20)
        win += 1
    if soma % 2 == 0 and op not in 'Pp':
        print('Deu PAR!')
        print('Você \033[1;33mPERDEU\033[m!!!')
        print('\033[1;34m+++++\033[m' * 20)
        break
    if soma % 2 == 1 and op not in 'Ii':
        print('Deu IMPAR!')
        print('Você \033[1;33mPERDEU\033[m!!!')
        print('\033[1;34m+++++\033[m' * 20)
        break
print(f'\033[1;31mGAME OVER\033[m! Você ganhou {win} vezes.')
