cont = 0
soma_idade = 0 #Variável para fazer a soma das idades
maior_idade_do_homem = 0
nome_velho = ''
mulheres_20anos = 0
for c in range(1,5):
    print ('-----{}ª PESSOA-----'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade #Vai fazer a somatória da idade de todas as pessoas
    cont += 1 
    media_idade = soma_idade / cont
    if c == 1 and sexo == 'M': 
        maior_idade_do_homem = idade
        nome_velho = nome 
    if sexo == 'M' and idade > maior_idade_do_homem:
        maior_idade_do_homem = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_20anos += 1 # Mostrar quantas mulheres tem menos de 20 anos
   
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_do_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres_20anos))