print('10 PRIMEIROS TERMOS DE UMA PA')
print('=-='*10)
n = int(input('Digite o primeiro termo : '))
razao = int(input('Digite a razão: '))
termo = n
cont = 1
print('Calculando a Progressão Aritmética desse número...')

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('ACABOU')
