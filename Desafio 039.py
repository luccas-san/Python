from datetime import date
atual = date.today().year
nasc = int(input('Informe o seu Ano de Nascimento: '))
idade = atual - nasc
print('Você tem {} anos'.format(idade))
if idade < 18:
    saldo = 18 - idade
    print('Você ainda não está na época do alistamento.')
    print('Ainda faltam {} anos para o seu alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será no ano de {}'.format(ano))
elif idade == 18:
    print('Você precisa se alistar \033[1;31mIMEDITAMENTE\033[m!')
elif idade > 18:
    saldo = idade - 18
    print('Você passou da idade para o Alistamento Militar!')
    print('Você deveria ter se alistado há {} anos atrás'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi no ano de {}'.format(ano))