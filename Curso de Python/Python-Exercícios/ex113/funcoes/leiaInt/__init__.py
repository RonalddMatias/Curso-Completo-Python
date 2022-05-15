def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[31mERRO: por favor, digite um número inteiro válido\033[m.')
            continue  # O CONTINUE VAI JOGAR PARA O LAÇO DE NOVO.
        except KeyboardInterrupt:
            # Quando o usuário não digitar nada (=clicar em control+c).
            print(
                '\033[31mERRO: o usuário não digitou nenhum número inteiro.\033[m')
            return 0
        else:
            return n