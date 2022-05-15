import time

print('''ESCOLHA UMA DAS OPÇÕES:
[ 1 ] Fazer uma contagem regressiva para a explosão
[ 2 ] Explodir imediatamente''')
valor = int(input('Qual das opções você escolhe?'))

if valor == 1:
    num = int(input('Digite um número: '))
    print('O ANO VAI VIRAR EM:')
    for x in range(num, -1, -1):
        print(x)
        print('---')
        time.sleep(1)
    print('FELIZ 2022, FELIZ ANO NOVO!!')
elif valor == 2:
    print('A BOMBA EXPLODIU IMEDIATAMENTE')
    print('Está tudo bem por aí? kkk')
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE MAIS TARDE.')

    
    