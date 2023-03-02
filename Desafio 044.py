preco = float(input('Informe o valor do Produto: R$'))
print("""Informe a forma de pagamento:
[ 1 ] Dinheiro/Cheque
[ 2 ] Cartão em 1x 
[ 3 ] Parcelado em 2x no Cartão
[ 4 ] Parcelado em 3x no Cartão""")
option = int(input('Informe a Opção de Pagamento: '))
if option == 1:
    desconto = preco - (preco * 10 / 100)
    print('O valor a ser pago em dinheiro com 10% de desconto será de R${:.2f}'.format(desconto))
elif option == 2:
    desconto = preco - (preco * 5 / 100)
    print('O valor a ser pago no Cartão com 5% de desconto será de R${:.2f}'.format(desconto))
elif option == 3:
    parcela = preco / 2
    print('Parcelado em 2x de R${:.2f} o valor será de {:.2f} sem juros'.format(parcela, preco))
    print('Essa forma de pagamento não possui desconto!')
elif option == 4:
    juros = preco + (preco * 20 / 100)
    parcela = int(input('Em quantas vezes quer parcelar? '))
    valor = juros / parcela
    print('Sua compra será parcelada em {}x no valor de R${:.2f}'.format(parcela, valor))
    print('Com essa forma de pagamento o valor será acrescido de 20% de juros.')
    print('Totalizando o valor de R${:.2f}'.format(juros))
else:
    print('Forma de pagamento Inválida. Tenta outra vez!')
