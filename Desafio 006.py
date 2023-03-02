n = int(input('Digite um Número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} é: {}.'.format(n, d))
print('O triplo de {} é: {}.'.format(n, t))
print('E a raiz quadrada de {} é: {:.2f}.'.format(n, r))
print('Vamos Continuar e aprender outra formatação?')
x = int(input('Digite outro Número: '))
print('O dobro de {} é: {}'.format(x,(x*2)))
print('O triplo de {} é: {} \nA raiz quadrada de {} é: {:.3f}'.format(x, (x*3), x, pow(x, (1/2))))
# Exercicio correto e concluido!
