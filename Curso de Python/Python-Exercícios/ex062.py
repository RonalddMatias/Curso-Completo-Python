print('10 PRIMEIROS TERMOS DE UMA PA')
print('=-='*10)
n = int(input('Digite o primeiro termo : '))
razao = int(input('Digite a razão: '))
termo = n
cont = 1
total = 0
mais = 10
print('Calculando a Progressão Aritmética desse número...')
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa', end= '')
    mais = int(input('\nQuantos termos você quer adicionar? '))
print('Ao todo foram mostrados {} termos nessa PA'.format(total))
