num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end= ' ')
        cont += 1
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(c), end=' ', )
print('\n\033[32mO número {} foi divido {} vezes.\033[m'.format(num, cont))

if cont == 2:
    print('O número {} é primo'.format(num))
else:
    print('O número {} não é primo'.format(num))