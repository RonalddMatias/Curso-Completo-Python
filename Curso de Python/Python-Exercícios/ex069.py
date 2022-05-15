contador = totHomens = totMulheres20 = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': #Enquanto o sexo não for masculino ou feminino, ele sempre vai repetir a pergunta.
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    escolha = ' ' 
    while escolha not in 'SN': #Enquanto a escolha não for sim ou não, ele vai sempre repetir a pergunta
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if idade >= 18:
        contador += 1 #Adicionar +1 a toda pessoa com +18 de idade
    if sexo == 'M':
        totHomens += 1 #adicionar +1 a toda pessoa que tenha o sexo masculino
    if sexo == 'F' and idade <20:
        totMulheres20 += 1 #Adicionar +1 a toda pessoa que seja mulher e que tenha menos de 20 anos.
    if escolha == 'N': 
        break #parar quando a escolha for igual a 'N'
    
print(f'\033[32mTOTAL DE PESSOAS COM MAIS DE 18 ANOS: {contador}')
print(f'AO TODO TEMOS {totHomens} HOMENS CADASTRADOS')
print(f'TEMOS {totMulheres20} MULHERES COM MENOS DE 20 ANOS\033[m')


 