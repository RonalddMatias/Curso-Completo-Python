dicionario = {}
dicionario['Nome'] = str(input('Nome: '))
media = dicionario['Media'] = float(input('Média: '))
for k, v in dicionario.items():
    print(f'O valor {k} é igual a {v}')
if media < 7:
    print('Situação é igual a Reprovado')
else:
    print('Situação é igual a Aprovado')
