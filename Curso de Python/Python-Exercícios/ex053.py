nome = str(input('Digite uma Frase: ')).strip().upper()
palavras = nome.split() #separar por espaços
junto = ''.join(palavras) #Juntar as palavras que foram separadas, agora sem espaços
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É um Palíndromo!')
else:
    print('Não é um Palíndromo!')