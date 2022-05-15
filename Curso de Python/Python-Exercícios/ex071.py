print('='*50)
print('{:^50}'.format('BANCO MATIAS'))
print('='*50)
valor = int(input('Que valor você que sacar? R$'))
total = valor
cedula = 50 #começar com a cédula de maior valor para o exercício
totcedula = 0 #Contabilizar quando cédulas foram retiradas
while True:
    if total >= cedula: #se o total for maior que o valor da cedula(R$50)
        total -= cedula #Vai retirar 50 desse valor quantas vezes forem necessarias
        totcedula += 1
    else: #Se não der para tirar R$50
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de R${cedula}')
        if cedula == 50: 
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print('='*30)
print('VOLTE SEMPRE AO BANCO MATIAS')