from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))  # CADASTRADO NO DIC
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc  # CADASTRADO NO DIC
# CADASTRADO NO DIC
dados['ctps'] = int(input('Carteira de Trabalho [0 não tem]: '))
# Dando uma condição para um dado dentro do dic, na qual só vai aparecer se o ctps for diferente de 0.
if dados['ctps'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print('-='*30)
for keys, valores in dados.items():
    print(f'    -{keys} tem o valor {valores}')
