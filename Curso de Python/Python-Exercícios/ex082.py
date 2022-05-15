lista = [] #Lista de Todos os números.
listaPar = [] #Lista de números pares.
listaImpar = [] #Lista de números ímpares.
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0: #Se o número dividido por dois der resto 0.
        listaPar.append(n) #adiciona na lista de números pares
    else:
        listaImpar.append(n) #adiciona na lista de números ímpares
    escolha = str(input('Quer continuar? [S/N]')).upper().strip()
    if escolha == 'N':
        break
print('=' * 30)
lista.sort()
print(f'A lista complera é: {lista}')
print(f'A lista de pares é: {listaPar}')
print(f'A lista de ímpares é: {listaImpar}')



