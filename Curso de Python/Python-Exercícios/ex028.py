import random
import time

print('-=-'*20)
#Perguntando ao usuário o número
numero = int(input('Digite um número no qual você acha que é o verdadeiro: '))
print('Processando...')
time.sleep(3) #Faz o computador simular que está esperando

#gerando um número de 1 a 5
num_secreto = random.randint(0,5) 

#Adicionando as condicionais
if numero == num_secreto:
    print('Parabéns, você acertou o número!')
else:
    print('Você errou, o número secreto era {}'.format(num_secreto))

print('-=-'*20)