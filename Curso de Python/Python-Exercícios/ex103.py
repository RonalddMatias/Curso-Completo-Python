def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


n = str(input('Qual o jogador? '))
g = str(input('Quantos gols ele fez? '))
if g.isnumeric():  # Verificar se a variavel g pode ser um número.
    g = int(g)  # Transforma g em um inteiro
else:
    g = 0  # adota g como 0
if n.strip() == '':  # Se eu tirei todos os espaços e ele ficou vazio
    ficha(gols=g)
else:
    ficha(n, g)
