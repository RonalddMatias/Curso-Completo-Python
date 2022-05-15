lista = []
n = media = contador = soma = 0
continuar = 'S'

while continuar == 'S':
    n = int(input('\033[32mDigite um número: \033[m'))
    continuar = str(input('\033[31mQuer continuar? [S/N] \033[m')).upper().strip()[0]
    contador += 1  # a cada novo número ele vai adicionar +1.
    soma += n  # A cada novo número ele vai somar os números posteriores.

    # A media foi feita pegando a soma de todos os termos (soma) e dividindo pela quantidade de termo(contaodor)
    media = soma / contador

    lista += [n]  # A cada novo número escrito ele vai adicionar na lista
print('=-='*20)
print('\033[32mVocê digitou {} número(s) e a média foi {:.2f}'.format(contador, media))
print('O maior valor foi {} e o menor foi {}\033[m'.format(max(lista), min(lista)))
print('\033[31mFim do Programa...\033[m')
print('=-='*20)
