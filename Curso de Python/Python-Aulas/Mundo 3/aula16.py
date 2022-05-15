lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
# print(lanche[2])
# print(lanche[1:3]) De 1 a 3 (lembrando que o python não conta o ultimo numero)
#print(lanche[2:]) #2 ATÉ O FINAL
# print(lanche[:2]) DO INICIO ATÉ 2

# print(sorted(lanche)) # --> ORDENA A TUPLA

# TRÊS MANEIRAS DIFERENTES DE USAR O FOR EM TUPLAS

# for comida in lanche:  # para cada comida no lanche
#    print(f'Eu vou comer {comida}')
#print(f'Comi pra caramba!')

# for posicao, comida in enumerate(lanche):  # para cada comida no lanche
#    print(f'Eu vou comer {comida} na posição {posicao}')
#print(f'Comi pra caramba!')

# for cont in range(0, len(lanche)):
#    print(f'eu vou comer {lanche[cont]} na posição {cont}.)

#a = (2, 5, 4)
# c = a + b  # vai juntar as tuplas
# print(c)
# print(c.count(9)) #QUANTAS VEZES O NÚMERO 5 APARECE EM C.
# print(c.index(5, 1))  # EM QUE POSIÇÃO ESTÁ O NÚMERO 5 DEPOIS DA POSIÇÃO 1

#pessoa = ('Gustavo', 38, 'M', 99.88)
# del(pessoa) #APAGAR UMA TUPLA INTEIRA
# print(pessoa)
