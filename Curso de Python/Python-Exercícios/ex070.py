print('-'*50)
print('LOJA SUPER BARATÃO'.center(50))
print('-'*50)

somador = maiormil = menorPreco = contador = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    contador += 1 # Adicionando +1 a cada produto adicionado
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    somador += preco #Somar tudo, total da compra
    if contador == 1 or preco < menorPreco: #Precisa apenas de uma primissa verdadeira
        menorPreco == preco
        barato == produto
    if preco > 1000:
        maiormil += 1 #Adicionar +1 a cada produto maior que 1000 reais
    if continuar == 'N': #Vai parar quando eu apertar 'N'
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${somador:.2f}')
print(f'Temos {contador} produto(s) custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menorPreco:.2f}')