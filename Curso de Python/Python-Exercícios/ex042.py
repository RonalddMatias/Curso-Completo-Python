#DUVIDAS NESSE DESAFIO
import time

lado1 = float(input('Digite o primeiro segmento: '))
lado2 = float(input('Digite o segundo segmento: '))
lado3 = float(input('Digite o terceiro segmento : '))

print('=' *50)
print('Processando se é capaz de formar um triangulo...')
time.sleep(3)
print('=' *50)

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    print('Com os lados {:.0f},{:.0f},{:.0f} será possível formar um triângulo.'.format(lado1,lado2,lado3))
    if lado1 == lado2 == lado3:
        print('Esses segmentos formará um triangulo EQUILÁTERO, na qual todos os lados são iguais.')
    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print('Esses segmentos formará um triângulo ESCALENO, na qual todos os lados são diferentes.')
    else:
        print('Esses segmentos formará um triângulo ISÓSCELES, na qual dois lados são iguais.')
else:
    print('Com os lados {:.0f},{:.0f},{:.0f} não será possível formar um triângulo.'. format(lado1,lado2,lado3))

