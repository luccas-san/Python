p = 0
maior = 0
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
while p != 5:
    print("""O que deseja fazer?
    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa""")
    option = int(input('Opção: '))
    if option == 1:
        print(f'A soma dos valores é {n1 + n2}')
    elif option == 2:
        print(f'A multiplicação dos valores é {n1 * n2}')
    elif option == 3:
        if maior < n1:
            maior = n1
        if maior < n2:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif option == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif option == 5:
        print('Adeus')
    else:
        print('Opção Invalida! Tente Novamente')