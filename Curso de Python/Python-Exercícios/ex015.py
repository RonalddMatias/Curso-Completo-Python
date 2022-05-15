from operator import indexOf
from zipapp import create_archive


print('====DESAFIO 15====')
dias = float(input('Digite quantos dias o carro foi alugado: '))
km = float(input('Digite quantos kilômetros o carro fez: '))
custo_pago = (dias * 60) + (km * 0.15)
print('O custo que será pago pelo carro que rodou {} dias e andou {} será de: R${}'.format(dias, km, custo_pago))