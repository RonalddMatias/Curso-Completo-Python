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


def linha(tam = 42):
    return '-'*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc