from pickle import TRUE
from re import T


n = soma = contador = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'A soma dos {contador} valores foi {soma}!')
print('Fim do Programa')
