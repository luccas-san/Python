frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um Palindromo!')
else:
    print('A frase digitada não é Palindromo!')
#Segunda Maneira:
#frase = str(int(input('Digite uma frase: ')).strip().upper()
#palavras = frase.split()
#junto = ' '.join(palavras)
#inverso = junto[::-1]
#print('O Inverso de {} é {}'.format(junto, inverso))
#if inverso == junto:
#   print('Temos um Palindromo')
#else:
#   print('A frase digitada não é um Palindromo!')