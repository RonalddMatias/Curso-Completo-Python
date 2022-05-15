sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MnFf':   # enquando sexo não estiver em 'MnFf'
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print('Sexo {} ragistrado com sucesso'.format(sexo))