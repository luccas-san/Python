nome = str(input('Informe o Nome do Aluno: ')).strip().title()
m1 = float(input('Digite a Nota da Primeira Matéria: '))
m2 = float(input('Digite a Nota da Segunda Matéria: '))
media = (m1 + m2)/2
print('A Média do Aluno {} é de {}'.format(nome, media))
if media < 5:
    print('O Aluno {} foi \033[1;31mREPROVADO\033[m!'.format(nome))
elif media == 5 or media <= 6.9:
    print('O Aluno {} está de \033[1;33mRECUPERAÇÃO\033[m!'.format(nome))
else:
    print('O Aluno {} foi \033[1;32mAPROVADO\033[m!'.format(nome))