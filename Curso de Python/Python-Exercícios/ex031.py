print('====DESAFIO 31====')

#variáveis
nome = str(input('Digite seu nome: '))
distancia = float(input('Digite a distância da viajem: '))
preco_1 = 0.5 * distancia
preco_2 = 0.45 * distancia

#Condicionais
print('A distância da viajem é {} km'.format(distancia))
if distancia <= 200:
    print('É uma viajem curta, o preço da passagem ficará de R$ {:.2f}'.format(preco_1))
else: 
    print('É uma viajem longa, o preço da viajem ficará de R$ {:.2f}'.format(preco_2))
print('Tenha uma boa viajem, {}.'.format(nome))