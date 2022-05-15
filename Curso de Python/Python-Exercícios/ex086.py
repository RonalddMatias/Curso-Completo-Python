matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#FOR DE ALIMENTAÇÃO
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30)
#FOR PARA PRINTAR NA TELA
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()  # quebrar a linha
