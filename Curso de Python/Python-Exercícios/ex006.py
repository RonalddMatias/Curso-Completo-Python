import math
print('\033[1;31m =====DESAFIO 06===== \033[m')
numero = int(input('Digite um número: '))
raiz = math.sqrt(numero)  # Raiz quadrada de um número
print(f'\033[35mO dobro desse número é: {numero*2}')
print(f'O triplo desse número é: {numero*3}')
print('A raiz quadrada desse número é: {:.2f} \033[m'.format(raiz))
