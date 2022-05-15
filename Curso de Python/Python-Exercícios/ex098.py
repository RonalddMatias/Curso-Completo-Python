from time import sleep
def contador(I, F, P):
    if P < 0: #Se o passo for negativo
        P *= -1 #vamos passar ele para positivo
    if P == 0:#Se o passo for igual a 0
        P=1 #Vamos passar ele para 1

    print('-='*20)
    print(f'Contagem de {I} até {F} de {P} em {P}.')
    sleep(2)

    if I < F:
        cont = I
        while cont <= F:  # Enquanto o contador for menor que o fim.
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += P #O contador vai recependo P 
        print('--> FIM')
    else: 
        cont = I
        while cont >= F:
            print(f'{cont}', end = ' ', flush=True) #Flusch serve para que o sleep funcione corretamente
            sleep(0.5)
            cont -= P #Vai sendo tirado do contador de acordo com o passo     
        print('FIM!')
    
    
# PROGRAMA PRINCIPAL
contador(1, 10, 1)  # de 1 até 10 de 1 em 1
contador(10, 0, 1)
print('-'*20)
print('AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM!')
ini = int(input('INÍCIO: '))
fin = int(input('FIM: '))
passo = int(input('PASSO: '))
contador(ini, fin, passo)
