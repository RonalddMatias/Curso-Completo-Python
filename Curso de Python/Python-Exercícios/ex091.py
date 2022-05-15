from random import randint
from time import sleep
from operator import itemgetter
# Gerano números aletórios para cada jogador
jogo = {'Jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'jogador4': randint(1, 6),
        }
ranking = {}  # Variavel para organizar os valores em ordem crescente.
print('Valores Sorteados: ')
# Lendo o Dicionário
for k, v in jogo.items():
    print(f'o {k} tirou {v} no dado.')
    sleep(1)
# O 1 foi por causa que é o resultado da key do dicionário jogo, assim, ordenando de forma decrescente.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)


# print(ranking)# Perceba no TERMINAL que esse print sai em forma de listas e tuplas, dessa forma vai ter que ser tratado como um lista e tuplas.
print('=-'*30)

print('==Ranking dos Jogadores==')
# Usando o enumerate pois é um lista e não um dictionary.:
for i, v in enumerate(ranking):
    print(f'    {i+1}º Lugar: {v[0]} com {v[1]}.')
    sleep(1)
