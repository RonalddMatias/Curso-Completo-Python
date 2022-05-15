from datetime import date

print('-=-' * 20)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=-' * 20)

#Definindo as variáveis
nome = str(input('Digite seu nome: '))
data_nascimento = int(input('Digite sua data de nascimento: '))
idade = date.today().year - data_nascimento

#Aplicando as condições aninhadas
if idade <= 9:
    print('Olá {}! você tem {} anos e faz parte da categoria MIRIM!'.format(nome, idade))
elif idade > 10 and idade <= 14:
    print('Olá {}! você tem {} anos e faz parte da categoria INFANTIL!'.format(nome, idade))
elif idade > 15 and idade <=19:
    print('Olá {}! você tem {} anos e faz parte da categoria JUNIOR!'.format(nome, idade))
elif idade > 19 and idade <= 20:
    print('Olá {}! você tem {} anos e faz parte da categoria SÊNIOR!'.format(nome, idade))
else:
    print('Olá {}! você tem {} anos e faz parte da categoria MASTER!'.format(nome, idade))