print('-'*35)
num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
print('-'*35)

if num_1 > num_2:
    print('\033[1;32mO número {} é maior que o número {}\033[m'.format(
        num_1, num_2))
elif num_2 > num_1:
    print('\033[1;32mO número {} é maior que o número {}\033[m'.format(
        num_2, num_1))
elif num_1 == num_2:
    75
    print('\033[1;32mEstes números são iguais\033[m')
else:
    print('\033[1;32mOpção Inválida\033[m')