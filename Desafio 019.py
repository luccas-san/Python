import random
n1 = str(input('Digite o nome do Primeiro Aluno: '))
n2 = str(input('Digite o nome do Segundo Aluno: '))
n3 = str(input('Digite o nome do Terceiro Aluno: '))
n4 = str(input('Digite o nome do Quarto Aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O Aluno escolhido foi: {} '.format(escolhido))

from random import choice
n5 = str(input('Digite o Nome do Primeiro Aluno: '))
n6 = str(input('Digite o Nome do Segundo Aluno: '))
n7 = str(input('Digite o Nome do Terceiro Aluno: '))
n8 = str(input('Digite o Nome do Quarto Aluno: '))
lis = [n5, n6, n7, n8]
choi = choice(lis)
print('O Aluno escolhido foi {}'.format(choi))
