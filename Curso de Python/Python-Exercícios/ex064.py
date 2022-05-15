n = soma = contador = 0
 #para desconsiderar o flag
while n != 999:
    n = int(input('Digite um número inteiro ou 999 para parar: '))
    if n != 999:
        soma += n #Toda vez que ele ler um número vai somar com o outro que será adicionado
        contador += 1 #Toda vez que ele ler um número vai ser adicionado +1
print('O total de números foi {} e a soma entre eles foi {}'.format(contador, soma))
    
