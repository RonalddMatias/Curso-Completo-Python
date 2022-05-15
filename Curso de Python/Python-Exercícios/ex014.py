print('====DESAFIO 14====')
celcius = float(input('informe a temperatura em °C: '))
faren = ((9*celcius)/5)+32  #formula que transforma celcius em fahrenheit
print('A temperatura de {}°C no Brasil, representa {:.2f}°F nos Estados Unidos'.format(celcius, faren))