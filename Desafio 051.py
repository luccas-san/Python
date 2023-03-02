primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 -1)* razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' ¬')
print('\033[1;32mACABOU\033[m')