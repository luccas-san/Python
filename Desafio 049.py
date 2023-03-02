#Refaça o Desafio/Challenge 009, mostrando a Tabuada de um número que o usuario escolher,
# só que agora utilizando o laço for.
n = int(input('Digite um Número para ver a sua Tabuada: '))
for c in range (1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
