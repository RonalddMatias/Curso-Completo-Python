print('====DESAFIO 08====')
num = float(input('Digite o número: '))
num_dec = num * 10
num_cent = num * 100
num_mili = num * 1000
num_km = num / 1000
num_hec = num / 100
num_dam = num / 10


print('\033[32m{} metros em milímetros é: {} km'.format(num, num_km))
print('{} metros em milímetros é: {} hec'.format(num, num_hec))
print('{} metros em milímetros é: {} dam'.format(num, num_dam))
print('{} metros em centimetros é: {:.0f} dm '.format(num, num_dec))
print('{} metros em centimetros é: {:.0f} cm '.format(num, num_cent))
print('{} metros em milímetros é: {:.0f} mm\033[m'.format(num, num_mili))
