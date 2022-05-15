from distutils import core


nome = 'Ronaldd'
cores = {'limpa':'\033[m' , 'azul':'\033[34m', 'Amarelo': '\033[33m', 'pretoebranco': '\033[7;30m' }

print('Olá, muito prazer em te conhecer, {}{}{}!'.format(cores['azul'], nome, cores['limpa'])) 