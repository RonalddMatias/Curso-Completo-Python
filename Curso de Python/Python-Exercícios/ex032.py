from datetime import date
print('====DESAFIO 32====')

ano = int(input('Que ano quer analisar? coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year #Para saber o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('O ano de de {} é um ano bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))