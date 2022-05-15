'''
teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:]) #Fazendo uma cópia de teste
teste[0]= 'Maria'
teste[1]= 22
galera.append(teste[:])
print(galera)
'''
#galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera[3][1])
#print(galera[2][0])
#for p in galera: #Para cada pessoa em galera
    #print(p[0]) # nome
    #print(p[1]) #Idade
    #print(f'{p[0]} tem {p[1]} anos de idade')

galera = []
dado = []
totmaior = totmenor = 0
for c in range(1,4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])#Tirar uma cópia do dado
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')


'''
lista = []
while True:
    lista.append(str(input('Digite seu nome: ')))
    lista.append(int(input('Digite sua idade: ')))
    escolha = str(input('Quer continuar? [S/N]')).strip().upper()
    if escolha == 'N':
        break
print(f'Esse são os elementos adicionados: {lista}')
'''
