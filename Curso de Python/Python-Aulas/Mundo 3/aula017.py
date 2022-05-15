#num = [2, 3, 5, 8, 2, 7]
#num[2] = 9
# num.append(7)
# num.sort(reverse=True) #ordenar ao contrario
# num.insert(2, 0) #Na posição 2 adicionar um 0
# num.pop() #Eliminar o ultimo valor da lista.
# num.pop(1)
# num.remove(2) #Elimina a primeira ocorrencia fo número 2 na lista
# if 4 in num: # Se 4 estiver em num
#    num.remove(4)
# else:
#    print('Não tinha o número quatro na lista')
# print(num)
#print(f'Essa lista tem {len(num)} elementos')


valores = []

for cont in range(1,5):
    valores.append(int(input(f'Digite o {cont} valor: ')))

for i, v in enumerate(valores): #vai dizer qual valor encontrou em cada posição
    print(f'Na posição {i} encontrei o valor {v}!')


#a = [2, 3, 4, 7]
#b = a #Ligação entre uma lista e outra
#b = a[:] #b receber todos os itens de A 9 (Fazer uma cópia)
#b[2] = 9
#print(f'Lista A: {a}')
#print(f'Lista B: {b}')


