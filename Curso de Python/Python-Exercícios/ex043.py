print('-=-'*30)
print('CALCULANDO O INDICE DE MASSA CORPOREA - IMC')
print('-=-'*30)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)

print ('Seu peso é {:.0f}Kg e sua altura é de {:.2f}m'.format(peso, altura))
print('Logo, o seu Índice de Massa Corpórea(IMC) é de {:.2f} Kg/m²'.format(imc))

if imc < 18.5:
    print('Isto significa que você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Isto significa que você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Isto signidica que você está em Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Isto significa que você está Obeso')
else:
    print('Isto significa que você está em Obesidade Mórbida')