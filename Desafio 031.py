km = float(input('Qual a distância da viagem em KM? '))
passagem1 = (km * 0.50)
passagem2 = (km * 0.45)
if km <= 200:
    print('O valor da passagem é R${:.2f}'.format(passagem1))
else:
    print('O valor da passagem é R${:.2f}'.format(passagem2))
print('-=-' * 35)
distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da passagem será de R${:.2f}'.format(preco))
print('-=-' * 35)
caminho = float(input('Qual a distância da sua viagem? '))
valor = caminho * 0.50 if caminho <= 200 else km * 0.45
print('O preço da passagem será de {:.2f}'.format(valor))