def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric(): #Se essa string poder ser numérica
            valor = int(n) #O valor vai passar a ser inteiro
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
        if ok:
            break
    return valor


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')