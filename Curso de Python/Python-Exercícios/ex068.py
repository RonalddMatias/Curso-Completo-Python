from random import randint
print('=-=' * 20)
print('Vamos jogar ÍMPAR ou PAR')
print('=-=' * 20)
contador = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um número: '))
    escolha = ' '
    total = computador + jogador
    while escolha not in 'PI':  # Enquanto a escolha não for par ou ímpar
        escolha = str(input('Escolha Ímpar ou Par: [P/I]')).strip().upper()
    print(
        f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    print('-'*20)
    if escolha == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU')
            contador += 1  # Contar quantas vezes ele ganhou
        else:
            print('VOCÊ PERDEU')
            break
    elif escolha == 'I':
        if total % 2 == 1:  # Vereficar se vc realmente ganhou
            print('VOCÊ VENCEU!')
            contador += 1
        else:
            print('VOCÊ PERDEU')
            break
    print('Vamos Jogar novamente')
    print('-'*20)
print(f'FIM DO JOGO! você venceu {contador} vezes')
