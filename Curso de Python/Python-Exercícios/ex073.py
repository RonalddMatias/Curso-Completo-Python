from time import sleep, time

print('-'*50)
print('{:^50}'.format('TABELA DO BRASILEIRÃO 2020'))
print('-'*50)

times = 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí'

print('''[ A ] Apenas os primeiros 5 colocados
[ B ] Apenas os últimos 4 colocados
[ C ] Ordem alfabética dos times
[ D ] Posição da Chapecoense
[ E ] Quem foi o campeão
[ F ] Sair''')
while True:
    opcao = str(input('Qual opção você deseja? ')).strip().upper()
    if opcao == 'A': #Caso clique em A
        for c in (times[0:5]):
            print(c)
    elif opcao == 'B': #Caso clique em B
        for x in (times[16:20]):
            print(x)
    elif opcao == 'C': #Caso clique em c
        print('Ordem Alfabética: ', end=' ')
        print(sorted(times))  # Organizar em Ordem Alfbética
    elif opcao == 'D': # Caso clique em D
        print('O time da chapecoense está em {} lugar'.format(times.index('Chapecoense')+1))
    elif opcao == 'E': #Caso clique em E
        print('O FLAMENGO FOI O CAMPEÃO BRASILEIRO DE 2020.')
    elif opcao == 'F': #Caso clique em F
        break
    else: # Caso não clique em nenhuma das opções anteriores
        print('Opção Inválida. Tente Novamente mais tarde.')
print('-'*50)
print('{:^50}'.format('FIM DO BRASILEIRÃO 2020'))
print('-'*50)



#print(f'Os primeiros 5 colocados são: \n{times[:5]}')
#print(f'Os 4 últimos colocados são: \n{times[16:20]}')
#print('Ordem Alfabética:', end=' ')
# print(sorted(times))
#print(f'A chapecoense está na posição {times.index(5)}')
