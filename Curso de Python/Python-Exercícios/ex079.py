lista = []
contador = 0
while True:
    num = int(input('Digite um valor: '))  # Vai adicionar o numero se:
    if num not in lista:  # o número não estiver na lista
        lista.append(num)
        print('Valor adicionado com sucesso')
    else:  # se o número estiver, não vai adicionar.
        print('Valor Duplicado! Não vou adicionar...')
        contador += 1
    escolha = str(input('Que continuar? [S/N]')).upper().strip()
    if escolha == 'N':
        break
print('-'*30)
lista.sort()  # Ordenar os valores.
print(f'Os valores adicionados foram {lista}')
if contador == 1:
    print(f'Tivemos {contador} valor que não foi adicionado para não ser repetido')
else:
    print(f'Tivemos {contador} valores que não foram adicionados para não serem repetidos')
