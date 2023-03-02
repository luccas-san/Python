nome = str(input('Digite seu nome Completo: ')).strip()
print('Analisando o seu Nome...')
print('Seu nome com maiusculas é: {}'.format(nome.upper()))
print('Seu nome com minusculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
# Primeiro Modo de Resolução:
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
# Segundo Modo de Resolução:
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))