r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos \033[1;32mPODEM FORMAR\033[m um triângulo.', end='')
    if r1 == r2 == r3:
        print('\033[1;33mEQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;34mESCALENO\033[m')
    else:
        print('\033[1;35mISÓSCELES\033[m')
else:
    print('Os segmentos \033[1;31mNÃO PODEM FORMAR\033[m um triângulo.')