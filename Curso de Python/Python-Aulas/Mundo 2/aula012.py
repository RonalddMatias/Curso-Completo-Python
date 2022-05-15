from traceback import print_tb


nome = str(input('Digite o seu nome: '))
if nome == 'Ronaldd':
    print('Que nome Lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')

print('Tenha um bom dia, {}'.format(nome))