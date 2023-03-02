while True:
    tab = int(input('Digite um valor para ver a sua Tabuada: '))
    print('==' * 20)
    if tab < 0:
        break
    for c in range (1, 11):
        print(f'{tab} x {c} = {tab * c}')
    print('==' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')