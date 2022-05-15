#pessoas = {'nome': 'Ronaldd', 'sexo': 'M', 'idade': 18}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.keys()) #printando as chaves
# print(pessoas.values())  # printando os valores
# print(pessoas.items()) #mostras chaves e valores

# for k in pessoas.keys():
#    print(k)
# for k in pessoas.values():
#    print(k)


# pessoas['nome']= 'Leandro' #trocando valores
# pessoas['peso']= 76.6 #adicionando valores
# for k, v in pessoas.items():  # PARA CADA KEYS E VALOR
#    print(F'{k} --> {v}')

# --------------------DICIONÁRIO DENTRO DE UMA LISTA -----------------
''''
brasil = []
estado1 = {'uf': 'rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
'''
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # copiando o dictionary para ser uma lista
for e in brasil:
    # for keys, valores in e.items():
    #    print(f'o campo {keys} tem valor {valores}.')
    for v in e.values():
        print(v)
