matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = terceiracoluna = maior = menor = 0
# ADICIONANDO OS VALORES NA MATRIZ
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para a casa [{l},{c}]: '))
# ORGANIZANDO A MATRIZ
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        # Printando valor por valor e centralizando a matriz.
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()  # QUEBRANDO LINHAS PARA UMA MATRIZ FICAR ORGANIZADA EM 3X3.
print('-='*30)
print(f'A soma de todos os valores pares digitados é: {spar}.')
# CALCULANDO A SOMA DA TERCEIRA COLUNA
for l in range(0, 3):
    # PERCEBA QUE A COLUNA É FIXA, APENAS A LINHA VAI MUDAR, QUE NESSE CADO VAI SER [0,2][1,2][2,2]
    terceiracoluna += matriz[l][2]
print(f'A soma da terceira coluna é igual a: {terceiracoluna}.')
# CALCULANDO O MAIOR NÚMERO DA SEGUNDA LINHA
for c in range(0, 3):
    if c == 0:
        # PERCEBA QUE NESSE CASO A LINHA 2 SEMPRE SERÁ [1].
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')
for c in range(0, 3):
    if c == 0:
        menor = matriz[2][c] #PERCEBA QUE O DOIS FICA FIXO PQ EU QUERO SABER APENAS DA LINHA 3.
    elif matriz[2][c] < menor:
        menor = matriz[2][c]
print(f'O menor valor da terceira linha é: {menor}')
