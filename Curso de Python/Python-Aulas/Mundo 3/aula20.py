# Adicionando Funções
'''
def lin():
    print('-'*30)
lin()
print('     Cadastro de Alunos      ')
lin()
'''
# FUNÇÕES COM TEXTOS
'''
def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)
mensagem('O FLAMENGO É O MELHOR TIME DO MUNDO.')
mensagem('O CORINTHIANS É UM MERDA.')
'''

'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# Programa Principal
soma(b=6, a=5)
'''

'''
def contador(* num):
    for v in num:
        print(v, end=' ')
    print('fim!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(1, 2, 3, 4)
contador(7, 3, 2)
'''
from typing import List


def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

#Programa Principal
valores = [6, 3, 5, 6, 7]
dobra(valores)
print(valores)
