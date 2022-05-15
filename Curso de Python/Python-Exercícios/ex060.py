
n = int(input('Digite um número: '))
c = n
f = 1  # sempre que for trabalhar com multiplicação bota o fator começando com 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
