'''for c in range(1, 7):
    print(c)
print('fim!')'''
'''
for c in range (6, 0, -1):
    print(c)
print('fim!')
'''
'''
i = int(input('ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')
'''
s = 0
contador = 0 
for c in range(1,201):
    if c % 2 == 0:
        contador += 1
        s += c
print('O somatório de {} número resultou em {}'.format(contador, s))