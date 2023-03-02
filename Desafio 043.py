peso = float(input('Informe o seu Peso: (kg) '))
altura = float(input('Informe a sua altura: (m) '))
imc = peso / (altura * altura)
print('Seu IMC é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está \033[1;33mABAIXO\033[m do peso')
elif imc <= 25:
    print('Você está no \033[1;32mPESO IDEAL\033[m')
elif imc <= 30:
    print('Você está com \033[1;31mSOBREPESO\033[m!')
elif imc <= 40:
    print('Você está em \033[1;31mOBESIDADE\033[m!')
else:
    print('Você está em \033[1;31mOBESIDADE MORBIDA.\033[m \033[1;33mCUIDADO!\033[m')