brasileiro = ('Atlético-MG', 'Flaamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
              'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR',
              'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('\033[1;32m+=\033[m\033[1;33m+=\033[m' * 30)
print(f'Lista de Times do Brasileirão: {brasileiro}')
print('\033[1;32m+=\033[m\033[1;33m+=\033[m' * 30)
print(f'Os 5 \033[1;32mPRIMEIROS\033[m colocados do Brasileirão 2021 são {brasileiro[0:5]}')
print('\033[1;32m+=\033[m\033[1;33m+=\033[m' * 30)
print(f'Os 4 \033[1;31mÚLTIMOS\033[m colocados do Brasileirão 2021 são {brasileiro[-4:]}')
print('\033[1;32m+=\033[m\033[1;33m+=\033[m' * 30)
print('A lista de times em ordem Alfabética é: ')
print(sorted(brasileiro))
print('\033[1;32m+=\033[m\033[1;33m+=\033[m' * 30)
print(f'A Chapecoense está na {brasileiro.index("Chapecoense")+1}ª posição')
print('\033[1;32m+=\033[m\033[1;33m+=\033[m' * 30)