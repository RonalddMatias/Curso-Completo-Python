print('='*30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('='*30)

p1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão:'))
decimo = p1 + (11-1) * razao  # formula universal


for x in range(p1, decimo, razao):
    print('{}'.format(x), end=' -> ')
print('ACABOU')
