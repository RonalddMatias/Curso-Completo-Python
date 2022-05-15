valores = []
mai = 0
men = 0
for n in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {n}: ')))
    if n == 0: #Se o primeiro valor que eu tô lendo
        mai = men = valores[n] #O primeiro valor lido é o maior e ao mesmo tempo é o menor
    else:
        if valores[n] > mai: #se os números que eu for adicionando for maior que o primeiro numero adicionado, então, ele (o maior númeor), vai passar a ser o número adicionado.
            mai = valores[n] #O MAIOR RECEBE ESSE VALOR.
        if valores[n] < men: #Se os números que eu for adicicionando for menor que o primeiro número adicionado, então, ele (o menor número), vai passar a ser o número adicionado.
            men = valores[n] #O MENOR RECEBE ESSE VALOR.

print('=-='*30)
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor digitado foi {mai} nas posições', end=' ')
for indice, valor in enumerate(valores):
    if valor == mai: #se o valor lido por ele for igual ao maior número, então ele vai printar o indice no qual ele se encontra.
        print(f'{indice}...', end=' ')
print()

print(f'O menor valor digitado foi {men} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == men: #Se o valor lido por ele for igual ao menor número, então ele vai printar o indice no qual ele se encontrar
        print(f'{indice}...', end=' ')
print()


