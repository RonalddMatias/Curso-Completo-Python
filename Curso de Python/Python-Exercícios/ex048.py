soma = 0 #ACUMULADOR
cont = 0
for c in range(1, 501, 2): #Gerando número de 1 até 500 de três em três
    if c % 3 == 0: #Só aparecer o números cujo o resto da divisão por três seja zero
        cont = cont + 1
        soma =  soma + c #Mostrar os números
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))