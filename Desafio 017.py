co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print('O Cateto Oposto mais o Cateto Adjacente tem a hipotenusa de: {:.2f}'.format(hi))

import math

ko = float(input('Digite outro Cateto Oposto: '))
ka = float(input('Digite outro Cateto Adjacente: '))
hip = math.hypot(ko, ka)
print('O resultado de Cateto Oposto mais Cateto Adjacente é: {:.2f}'.format(hip))

from math import hypot
import emoji

cco = float(input('Digite o Valor do Cateto Oposto: '))
cca = float(input('Digite o Valor do Cateto Adjacente: '))
hipo = hypot(cco, cca)
print('O resultado do Cateto Oposto mais o Cateto Adjacente é: {:.2f}'.format(hipo))
print('Você consegui chegar a mais uma Desafio Finalizado. Continue!')
