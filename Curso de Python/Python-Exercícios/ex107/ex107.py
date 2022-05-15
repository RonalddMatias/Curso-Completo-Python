import moeda

n = float(input('Digite um preço: R$ '))
print(f'A metade de {n} é {moeda.metade(n)}')
print(f'O dobro de {n} é {moeda.dobro(n)}')
print(f'o valor de {n} aumentado em 10% é {moeda.aumentar(n):.2f}')
print(f'O valor de {n} diminuido em 13% {moeda.reduzir(n):.2f}')
