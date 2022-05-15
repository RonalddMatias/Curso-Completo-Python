from random import randint
from time import sleep
print('-'*60)
print('{:^60}'.format('JOGO DA MEGA SENA'))
print('-'*60)

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
lista = []
jogos = []
tot = 1
# So vai parar quando o tot se igualar ao número escrito pelo usuário.
while tot <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)  # GERAR NÚMEROS ALEATÓRIOS.
        if num not in lista:  # Se o número adicionado aleatoriamente não estiver na lista
            lista.append(num)  # Adiciona-lo na lista.
            cont += 1
        if cont >= 6:  # Parar quando sortear 6 números aleatórios.
            break
    lista.sort()  # ORDENANDO
    # Fazendo uma cópia para as listas ficanrem adicionadas dentro de apenas UMA lista.
    jogos.append(lista[:])
    lista.clear()  # Limpando a lista para não ficar adicionando sempre.
    tot += 1

print(f'Sorteando {quantidade} jogos...')

for indice, valor in enumerate(jogos):
    print(f'Jogo {indice+1}: {valor}') #O Indice será a lista que tiver nas posições e o valor é o resultado que tem dentro dela
    sleep(1)
print('{:-^60}'.format('BOA SORTE'))
