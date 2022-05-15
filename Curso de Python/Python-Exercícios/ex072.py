numeros = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze','Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove','Vinte')


while True:
    n = int(input('DIGITE UM NÚMERO ENTRE 0 E 20: '))
    while n < 0 or n > 20:# Enquanto o número for maior que 20 e menor que 0, o programa vai mandar digitar novamente até estar entre 0 e
        n = int(input('TENTE NOVAMENTE.DIGITE UM NÚMERO ENTRE 0 E 20: '))
    print(f'O número digitado foi {numeros[n]}') #Printar o número na posição que eu indicar da tupla
    continuar = str(input('Desaja continuar? ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? ')).strip().upper()[0] #perguntar até ele digitar sim ou não
    if continuar == 'N': #parar quando eu digitar 'N'
        break
print('FIM DO PROGRAMA')
