import moeda

n = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'o valor de {moeda.moeda(n)} aumentado em 10% é {moeda.moeda(moeda.aumentar(n))}')
print(f'O valor de {moeda.moeda(n)} diminuido em 13% {moeda.moeda(moeda.reduzir(n))}')
