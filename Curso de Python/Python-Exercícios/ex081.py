lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    escolha = str(input('Quer continuar? [S/N]')).upper().strip()
    if escolha == 'N':
        break
print(f'Você digitou {len(lista)} elementos')  # Saber o tamanho da lista
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 not in lista:  # Se o número 5 não estiver na lista:
    print('O valor 5 não faz parte da lista') #printar isso
else: #se tiver:
    print('O valor 5 faz parte da lista')
