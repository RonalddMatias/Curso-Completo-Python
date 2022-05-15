galera = []
pessoa = {}
somador = contador = 0
while True:
    pessoa.clear() #Limpando para não repetir
    pessoa['Nome'] = str(input('Nome: '))
    while True: 
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        else:
            print('ERRO. POR FAVOR, DIGITE M OU F.')    
    pessoa['idade'] = int(input('Idade: '))
    somador += pessoa['idade']
    galera.append(pessoa.copy()) #Recebendo uma cópia de pessoa.
    while True:
        resposta = str(input('Quer continuar? [S/N]')).upper()[0]
        if resposta in 'SN':
            break #Para dois while é necessário dois break's.
        else: 
            print('ERRO. POR FAVOR, DIGITE S OU N.')
    if resposta == 'N':
        break
media = somador / len(galera)
print('-='*30)
print(galera)
print(f'A) Ao todo, foram cadastradas {len(galera)} pessoas.')
print(f'B) A média das pessoas cadastradas foi de {media:.1f} anos')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'    -{p["Nome"]}', end='')
    print() #Quebrar de linha
print (' D) lista das pessoas que estão acima da média: ',end='')
for p in galera:
    if p['idade'] > media:
        print(f'    -{p["Nome"]}',end='')
    print() #Quebrar Linha
print('<< ENCERRADO >>')