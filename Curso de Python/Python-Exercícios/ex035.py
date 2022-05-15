#DESAFIO DA FORMAÇÃO DE UM TRIANGULO
print('====DESAFIO 35====')
lado_1 = float(input('\033[1;32mPrimeiro Lado: \033[m'))
lado_2 = float(input('\033[1;32mSegundo Lado: \033[m'))
lado_3 = float(input('\033[1;32mTerceiro Lado: \033[m'))

if lado_1 < lado_2 +lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_2 + lado_1:
    print('\033[31mCom os lados {:.0f},{:.0f},{:.0f}, é possível formar um triângulo \033[m'.format(lado_1, lado_2, lado_3))
else:
    print('Com os lados {:.0f},{:.0f},{:.0f}, não é possível formar um triângulo'.format(lado_1, lado_2, lado_3))