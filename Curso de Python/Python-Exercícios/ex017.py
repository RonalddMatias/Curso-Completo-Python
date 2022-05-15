from math import hypot
cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('O triangulo tem {} de cateto oposto e {} de cateto adjacente, assim, o valor da sua hipotenusa será de: {:.2f}'.format(cateto_oposto, cateto_adjacente,hipotenusa))