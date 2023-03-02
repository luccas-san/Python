import random
n1 = str(input('Digite o Primeiro Nome: '))
n2 = str(input('Digite o Segundo Nome: '))
n3 = str(input('Digite o Terceiro Nome: '))
n4 = str(input('Digite o Quarto Nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem da Apresentação será: ')
print(lista)

from random import shuffle
n6 = str(input('Digite o nome de um Primeiro Aluno: '))
n7 = str(input('Digite o nome de um Segundo Aluno: '))
n8 = str(input('Digite o nome de um Terceiro Aluno: '))
n9 = str(input('Digite o nome de um Quarto Aluno: '))
lis = [n6, n7, n8, n9]
shuffle(lis)
print('A nova ordem de sorteio é: ')
print(lis)