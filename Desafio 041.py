from datetime import date
atual = date.today().year
ano = int(input('Informe o Ano de Nascimento: '))
idade = atual - ano
if idade <= 9:
    print('O Atleta tem {} anos. Ele é Categoria MIRIM'.format(idade))
elif idade == 9 or idade <= 14:
    print('O Atleta tem {} anos. Ele é Categoria INFANTIL'.format(idade))
elif idade == 14 or idade <= 19:
    print('O Atleta tem {} anos. Ele é Categoria JUNIOR'.format(idade))
elif idade == 19 or idade <= 25:
    print('O Atleta tem {} anos. Ele é Categoria SÊNIOR'.format(idade))
else:
    print('O Atleta tem {} anos. Ele é Categoria MASTER'.format(idade))
# Outra Maneira:
#from datetime import date
#atual = date.today(). year
#nascimento = int(input('Ano de Nascimento:'))
#idade = atual - nascimento
#print('O Atleta tem {} anos.'.format(idade))
#if idade <= 9:
#   print('Classificação: MIRIM')
#elif idade <= 14:
#   print('Classificação: INFANTIL')
#elif idade <= 19:
#   print('Classificação: JUNIOR')
#elif idade <= 25:
#   print('Classificação: SÊNIOR')
#else:
#   print('Classificação: MASTER')