from time import sleep
sleep(1)
print('-=-' * 20)
print('Bem-Vindo ao Sistema de Transito')
print('-=-' * 20)
sleep(1)
nome = str(input('Informe o nome do motorista: ')).strip().capitalize()
sleep(1)
km = float(input('Informe qual a velocidade em que ele estava: '))
multa = (km - 80 ) * 7
if km <= 80:
    print('O Motorista não foi multado!')
    sleep(1)
    print('Dirija com Cuidado!')
else:
    print('O Motorista foi multado!')
    sleep(1)
    print('Calculando o valor da Multa...')
    sleep(1)
    print('O valor da multa é R${:.2f}'.format(multa))