num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        cont = cont + 1
        soma = num + soma
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))
