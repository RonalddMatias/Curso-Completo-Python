
from time import sleep


def maior(* num): # Isso se chama 'Desempacotamento', na qual a função pode receber vários parâmetros.
    contador = maior = 0
    print('-='*30)
    print(f'ANALISANDO OS VALORES PASSADOS...')
    for valor in num:
        # Esse flush serve para que o sleep funcione corretamente
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    print()


# Programa Principal
maior(2, 9, 3, 4, 5, 6)
maior(1, 2)
maior(6)
maior()
