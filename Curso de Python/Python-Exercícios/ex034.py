print('====DESAFIO 34====')

salario = float(input('Digite o seu salário: '))
print('O salário que você recebe é de R$ {:.0f}'.format(salario))

aumento_1 = salario * 1.1
aumento_2 = salario * 1.15

if salario <= 1250:
    print('Você ganhou um aumento de 15%, agora o seu seu salário ficará de R${:.2f}'.format(aumento_2))
else:
    print('Você ganhou um aumento de 10%, agora o seu seu salário ficará de R${:.2f}'.format(aumento_1))
print('Parabéns pelo aumento, continue assim!')
