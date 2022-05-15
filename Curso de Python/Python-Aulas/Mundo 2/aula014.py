'''c = 1  # CONTADOR
while c < 11:
    print(c)
    c += 1
print('fim')'''

'''
r = 'S'
while r == 'S': #fleg = condição de parada
    n = int(input('Digite um Número: '))
    r = str(input('Quer Continuar? [S/N]')).upper()
print('Fim')
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: #NÃO CONTAR O 0 COMO NÚMERO IMPAR
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('A quantidade de número(s) par é: {} \nA quantidade de número(s) impar é: {}'.format(par, impar))