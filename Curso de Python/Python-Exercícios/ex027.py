from traceback import print_tb


print('====DESAFIO 27====')
frase = str(input('Digite seu nome: ')).strip()
nome = frase.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu penultimo nome é: {}'.format(nome[len(nome)-2]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))