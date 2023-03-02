salario = float (input('Digite seu salario R$ '))
novo = salario + (salario * 15/100)
print('Antes do aumento você recebia mensalmente R${:.2f}. Agora com 15% de aumento você passará a receber R${:.2f}'
      .format(salario, novo))