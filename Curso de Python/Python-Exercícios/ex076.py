listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Tranferidor',
            4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇO'))
print('-'*50)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:#O número que o resto da divisão por 2 é 0, representa os nomes
        print(f'{listagem[pos]:.<30}', end='')
    else: # Os números que não são divisiveis por 2 representa os números
        print(f'R${listagem[pos]:>7.2f}')
print('-'*50)