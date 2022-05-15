#EXECICIO 93 APRIMORADO
time = []
dados = {}
partidas = []
while True:
    dados.clear() #Apagar o dicionario lido para não repeti-lo dentro da lista
    dados['Nome'] = str(input('Nome do Jogador: '))
    total = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0,total):
        partidas.append(int(input(f'    -Quantos gols na primeira {c+1} partida?'))) 
    dados['gols'] = partidas[:] #A chave gols recebe partida, fazendo com que fique uma lista dentro do dicionário
    dados['total'] = sum(dados['gols']) #Somando os gols
    time.append(dados.copy()) #copiando o dicionário 'dados' para a lista 'time'.

    while True: 
        escolha = str(input('Quer Continuar? [S/N]')).upper()[0]
        if escolha in 'SN':
            break
        else:
            print('ERRTO! RESPONDA COM S OU N.')
    if escolha == 'N':
        break
print('-='*30)
#cabeçalho
print('cod', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()

print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ' )
        for k, v in enumerate(time[busca]['gols']):
            print(f'    No jogo {k+1} fez {v} gols')
    print('-'*30)
print('<<< VOLTE SEMPRE >>>')
