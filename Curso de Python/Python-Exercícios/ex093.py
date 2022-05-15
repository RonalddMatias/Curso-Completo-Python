dados = {}
partidas = []
dados['Nome'] = str(input('Nome do Jogador: '))
total = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0,total):
    partidas.append(int(input(f'    -Quantos gols na primeira {c+1} partida?'))) 
dados['gols'] = partidas[:] #A chave gols recebe partida, fazendo com que fique uma lista dentro do dicionário
dados['total'] = sum(dados['gols']) #Somando os gols
print('-='*30)
print(dados)
print('-='*30)
for keys, valores in dados.items():
    print(f'O campo {keys} tem o valor {valores}.')
print('-='*30)
print(f'O jogador {dados["Nome"]} jogou {len(dados["gols"])} partidas')

for indice, valor in enumerate(dados['gols']): #PEGANDO APENAS DA LISTA, ALIAS, ESSE METODO DE ENUMERATE SÓ PODE SER UTILIZADO EM LISTAS E TUPLAS.
    print(f'    -->Na partida {indice+1}, fez {valor} gols')
print(f'Foi um total de {dados["total"]} gols')