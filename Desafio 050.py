soma = 0
cont = 0
for n in range (1 , 7):
    num = int(input('Digite o {}° valor: '.format(n)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('A Soma dos {} valores \033[1;32mPARES\033[m é {}'.format(cont, soma))