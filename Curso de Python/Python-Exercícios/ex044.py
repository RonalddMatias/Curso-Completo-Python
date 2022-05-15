print('{:=^40}'.format(' LOJAS MATIAS '))
preco = float(input('Qual foi o valor das compras: R$'))
print('''FORMA DE PAGAMENTO:
[ 1 ] À vista dinherio/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco * 0.9
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(
        'Sua compra será parcelada em 2x de R${:.2F} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (20/100 * preco)
    totalParcela = int(input('Quantas Parcela? '))
    parcela = total / totalParcela
    print('Sua compra será parcelada em {} de R${:.2F} COM JUROS'.format(
        totalParcela, parcela))
else:
    total = preco
    print('Opção Inválida de Pagamento')

print('Sua compra de R${:.2f} vai custar R${} no final.'.format(preco, total))
