real = float(input('Quanto dinheiro você tem na carteira R$?'))
dolar = real / 5.25
euro = real / 6.16
libra = real / 7.20
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar £{:.2f}'.format(real, euro))
print('Com R${:.2f} você pode comprar L£{:.2f}'.format(real, libra))
#Exercicio Correto e Concluido
