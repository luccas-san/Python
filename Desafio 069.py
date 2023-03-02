maior = 0
homem = 0
menordeidade = 0
from time import sleep
while True:
    print('---' * 20)
    print('CADASTRE UMA PESSOA')
    print('---' * 20)
    idade = int(input('Qual a idade? '))
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MmFf':
        print('Informe um valor válido!')
        sleep(2)
        sexo = str(input('Informe novamente [M/F]: '))
    print('****' * 25)
    option = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while option not in 'SsNn':
        print('Informe um valor válido!')
        sleep(2)
        option = str(input('Informe novamente. Deseja continuar [S/N]: ')).strip().upper()[0]
    print('****' * 25)
    if idade > 18:
        maior += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        menordeidade += 1
    if option in 'Nn':
        break
print(f'Ao total existem {maior} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {homem} homens.')
print(f'Existem {menordeidade} mulheres menores de 20 anos.')