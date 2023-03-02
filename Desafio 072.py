numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros[num]}')
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if op in 'S':
            continue
        if op in 'N':
            break
    if num < 0 or num > 20:
        print('Número Invalido!',end=' ')
print('Fim! Volte Sempre...')
