#COM O PESO
temporaria = []
principal = []
maiorPeso = menorPeso = 0
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        menorPeso = maiorPeso = temporaria[1]
    else:
        if temporaria[1] > maiorPeso:
            maiorPeso = temporaria[1]
        if temporaria[1] < menorPeso:
            menorPeso = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    escolha = str(input('Quer continuar? [S/N]')).upper().strip()
    if escolha == 'N':
        break

# o LEN vai informar o tamanho.
print(f'{len(principal)} pessoas foram cadastradas')
print(f'O maior peso é {maiorPeso:.2f}Kg. Peso de :', end='')
for c in principal:  # varre a lista, analisando número por número.
    if c[1] == maiorPeso:
        # TEMPORARIA[0] É O NOME DA PESSOA QUE VAI TER O PESSO IGUAL A VARIÁVEL 'maiorPeso'
        print(f'[{c[0]}] ', end='')
print(f'\nO menor peso é {menorPeso:.2f}Kg. Peso de:', end='')
for c in principal: #Varrer a lista, analisando número por número.
    if c[1] == menorPeso:
        print(f'[{c[0]}]', end = '')
