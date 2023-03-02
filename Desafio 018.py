from math import radians, sin, cos, tan
an = float(input('Digite o Angulo que você deseja: '))
se = sin(radians(an))
print('O Angulo de {} tem o SENO de: {:.2f}'.format(an, se))
coss = cos(radians(an))
print('O Angulo de {} tem o Cosseno de: {:.2f}'.format(an, coss))
tan = tan(radians(an))
print('O Angulo de {} tem a Tangente de: {:.2f}'.format(an, tan))

import math
ang = float(input('Digite outro Angulo diferente: '))
seno = math.sin(math.radians(ang))
print('O Angulo de {} tem o SENO de: {:.2f}'.format(ang, seno))
cosseno = math.cos(math.radians(ang))
print('O Angulo de {} tem o Cosseno de: {:.2f}'.format(ang, cosseno))
tang = math.tan(math.radians(ang))
print('O Angulo de {} tem a Tangente de: {:.2f}'.format(ang, tang))
print('Mais um Exercicio Finalizado. Congratulations!!!')