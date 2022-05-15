print('-=-'*20)
print('Seja Bem Vindo! Informaremos se seu empréstimo será aprovado.')
print('-=-'*20)

nome = str(input('Digite seu nome: '))
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Digite a quantidade de anos na qual você quer pagar: '))

valor_prestacao = casa / (anos * 12)
excedente = salario * (30/100)


print('-'*150)
print('\033[32mOlá {}! você nos informou que o valor da casa será de R${:.0f} e que o seu salário é de R${:.0f}, na qual você vai pagar em {} anos.\033[m'.format(nome, casa, salario, anos))
print('-'*150)

print('O valor da prestação mensal ficará de R${:.2f}'.format(valor_prestacao))
if valor_prestacao > excedente:
    print('\033[31mInfelizmente o seu empréstimo foi negado\033[m')
else:
    print('\033[32mAnalisamos a sua solicitação {}, o seu empréstimo foi aprovado!\033[m'.format(nome))
