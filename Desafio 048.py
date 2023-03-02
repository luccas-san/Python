# Faça um programa que calcule a some entre todos os numeros impares que são multiplos de tres
# e que se encontram no intervalo de 1 ate 500.
soma = 0
cont = 0
for c in range(1 , 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma dos {} valores é igual a {}'.format(cont, soma))