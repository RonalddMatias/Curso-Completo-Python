print('====DESAFIO 29====')
velocidade = float(input('Digite a velocidade em que você estava: '))
multa = 7 * (velocidade - 80)
print('Você estava a {} km/h'.format(velocidade))
print('O limite da rodovia é de 80 km/h')

if velocidade <= 80:
    print('Você estava dentro do limite permitido na rodovia, não haverá multa.')
else:
    print('Você estava acima do limite permitido na rodovia, a sua multa será efetuada no valor de: R${:.2f}'.format(multa))
