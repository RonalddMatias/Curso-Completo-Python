print('====DESAFIO 11====')
num_altura = float(input('Digite o número da altura da parede: '))
num_largura = float(input('Digite o número da largura da parede: '))
area = num_altura * num_largura
print('Sua parede tem dimensões de {} x {} e a sua área é de {:.2f}m²'.format(num_altura, num_largura, area))
tinta = area / 2
print('o número de litros necessários para pintar a parede é {:.1f} L'.format(tinta))