print('====DESAFIO 12====')
preco = float(input('Qual o preço do produto: '))
desconto = preco * 0.95
print('O produto que estava por R${}, agora na liquidação de 5% vai estar por R${:.2f}'.format(preco, desconto))

#O ":.2f" é para limitar a quantidade de casa após a virgula