def leiaFloat(msg):
    while True:
        try:  # TENTE
            n = float(input(msg))
        except (ValueError, TypeError):  # SE DER ERRADO
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print(
                '\033[31mERRO: O usuário preferiu não digitar nenhum número real.\033[m')
            return 0
        else:  # SE DER CERTO
            return n