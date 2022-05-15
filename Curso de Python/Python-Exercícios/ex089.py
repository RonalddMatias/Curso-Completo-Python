from ctypes.wintypes import INT


listaprincipal = []

while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    listaprincipal.append([nome, [nota1, nota2], media])
    escolha = str(input('Quer Continuar? [S/N]')).upper().strip()
    if escolha == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')  # ALINHANDO OS CARACTERES.
print('-'*30)
for indice, valor in enumerate(listaprincipal):
    # Mostrando o índice, o nome da pessoa e o valor da média. Alinhando sempre de acordo com a sentença acima.
    print(f'{indice:<4} {valor[0]:<10} {valor[2]:>8.1f}')
while True:
    print('-' * 26)
    opc = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(listaprincipal) - 1: #O -1 é pq a contagem começa em 0.
        print(f'Notas de {listaprincipal[opc][0]} são {listaprincipal[opc][1]}')
    else:
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
print('<<< VOLTE SEMPRE >>>')