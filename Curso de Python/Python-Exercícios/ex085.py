num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o número: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort() #Organizar em ordem crescente a primeira lista
num[1].sort()#Organizar em ordem crescente a segunda lista
print(f'A lista dos números ímpares --> {num[1]}')
print(f'A lista dos número pares --> {num[0]} ')