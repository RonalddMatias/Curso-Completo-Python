#COM A IDADE
temp = []
prin = []
maisVelho = maisNovo = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Idade: ')))

    if len(prin) == 0:
        maisVelho = maisNovo = temp[1]
    else:
        if temp[1] > maisVelho:
            maisVelho = temp[1]
        if temp[1] < maisNovo:
            maisNovo = temp[1]

    prin.append(temp[:])
    temp.clear()  # O CLEAR É NECESSÁRIO PARA ADICIONAR LISTAS DENTRO DE UMA LISTA
    escolha = str(input('Quer Continuar? [S/N]')).upper().strip()
    if escolha == 'N':
        break

print(f'Foram cadastras {len(prin)} pessoas')
print(f'A maior idade é {maisVelho} anos. Pertencente à: ', end='')
for p in prin:
    if p[1] == maisVelho: #A idade que for igual ao mais velho ele vai printar o nome.
        print(f'[{p[0]}]', end='')
print(f'\nA menor idade é {maisNovo} anos. Pertencente à: ', end='')
for p in prin:
    if p[1] == maisNovo:
        print(f'[{p[0]}]',end='')
