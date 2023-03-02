from datetime import date
hoje = date.today().year
cont = 0
conta = 0
for i in range(1, 8):
    nasc = int(input('Informe o Ano de Nascimento da {}° Pessoa: '.format(i)))
    ano = hoje - nasc
    maior = ano >= 21
    menor = ano < 21
    if menor:
        cont = cont + 1
    elif maior:
        conta = conta + 1
print('Você tem \033[1;34m{}\033[m pessoas no seu Grupo.'.format(i))
print('{} ainda \033[1;31mNÃO ATIGIRAM\033[m a maior idade e '.format(cont), end='')
print('{} já são \033[1;32mMAIORES\033[m de idade.'.format(conta))
