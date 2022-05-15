from time import sleep


n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior Valor
    [ 4 ] Novos Números
    [ 5 ] Sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    print ('=-='*10)
    if opcao == 1:
        print('\033[31mA soma é igual a {}\033[m'.format(n1 + n2))
    elif opcao ==2:
        print('\033[31mA multiplicação é igual a {}\033[m'.format(n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('\033[31mO número {} é maior que o {}\033[m'.format(n1, n2))
        elif n2 > n1:
            print('\033[31mO número {} é maior que o {}\033[m'.format(n2, n1))
        else:
            print('\033[31mOs números são iguais\033[m')
    elif opcao == 4:
        print('\033[31mInforme os números novamente: \033[m')
        n1 = int(input('\033[31mPrimeiro Número:  \033[m'))
        n2 = int(input('\033[31mSeguno Número: \033[m'))
    elif opcao == 5:
        sleep(3)
        print('\033[32mFinalizando...\033[m')
    else:
        print('Opção Inválida')
print('\033[32mFim do Programa\033[m')