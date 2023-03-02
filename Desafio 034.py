salario = float(input('Informe o salario do funcioario: R$ '))
aumento1 = salario + (salario * 15 / 100)
aumento2 = salario + (salario * 10 / 100)
if salario <= 1250:
    print('O salario foi aumentado em 15%. Ficando com o valor de {:.2f}'.format(aumento1))
else:
    print('O salario foi aumentado em 10%. Ficando com o valor de {:.2f}'.format(aumento2))

