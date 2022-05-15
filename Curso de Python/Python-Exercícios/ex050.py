soma = 0 #Acumulador
cont = 0 #Contador
for p in range(1,7):
    num = int(input('Digite um {} numero inteiro: '.format(p)))
    if num % 2 == 0: #O
        soma += num
        cont += 1
print('\033[32mA soma de {} números pares será de {}\033[m'.format(cont, soma))