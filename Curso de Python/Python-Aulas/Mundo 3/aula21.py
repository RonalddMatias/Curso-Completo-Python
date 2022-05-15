'''
# Inserindo uma docstring
def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela
    i: Inicio da Contagem
    f:Fim da contagem
    p: Passo da contagem
    return: sem retorno
    Função criada por Ronaldd Matias
    """
    cont = i
    while cont <= f:
        print(f'{cont}', end=' ')
        cont += p
    print('--> Fim!')

help(contador)
'''

'''
# Parâmetros Opcionais

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(1)
somar(0)
somar(1,2)
'''

# Escopo de Variáveis

'''
def teste():
    global n -->  ****DUVIDAS****
    x = 8  # VARIAVEL DE ESCOPO LOCAL
    n = 5
    print(f'Na função teste, n dentro vale {n}.')
    print(f'Na função teste, o x dentro vale {x}.')


n = 2  # VARIAVEL DE ESCOPO GLOBAL
print(f'Na função teste, n fora vale {n}.')
teste()
#print(f'Na função teste, o x vale {x}')
'''

'''
#Retornando Valores 
def somar(a=0,b=0,c=0):
    s = a + b + c
    return s


r1 = somar(1,2,4)
r2 = somar(2,3,9)
r3 = somar(0,0,5)
print(f'Meus cálculos dera {r1}, {r2} e {r3}.')
print(somar(1,2,8))
'''

'''
def fatorial(num=1):
    f = 1  # VARIÁVEL DE ESCOPO LOCAL.
    for c in range(num, 0, -1):  # começa no número e vai voltando.
        f *= c  # Multiplica todos os valores.
    return f


n = int(input('Digite um número: ')) #VARIAVEL DE ESCOPO GLOBAL.
print(f'O fatorial de {n} é {fatorial(n)}.')
'''


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('é Par!')
else:
    print('Não é Par!')
