dias = int(input('Quantos dias o automovel ficou alugado? '))
km = float(input('Quantos KM percorridos? '))
pago = (dias*60) + (km*0.15)
print('O valor a ser pago é R${}'.format(pago))