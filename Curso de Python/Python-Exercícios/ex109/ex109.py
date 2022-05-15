import moeda

n = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'o valor de {moeda.moeda(n)} aumentado em 10% é {moeda.aumentar(n, True)}')
print(f'O valor de {moeda.moeda(n)} diminuido em 13% {moeda.reduzir(n, True)}')
#Esse true é um parametro opcional na qual o valor númerico vai aparecer formatado.