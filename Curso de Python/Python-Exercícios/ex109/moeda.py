def metade(n = 0, formato = False):
    res = n / 2
    return res if formato is False else moeda(res)
    #Vai retornar res(sem formatação) se o formato for false, se não, vai retornar o valor formatado.
    #O 'moeda(res)' é uma função do proprio modulo, se estivesse em outro local teria que importar.

def dobro(n = 0, formato = False):
    res = n * 2
    return res if formato is False else moeda(res)

def aumentar(n = 0, formato = False):
    s = n * 1.1
    return s if formato is False else moeda(s) #aumentar 10%

def reduzir(n = 0, formato = False):
    s = n * 0.87 #diminuir 13%
    return s if formato is False else moeda(s)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',') #Replace é para substituir, nesse caso vai substituir um ponto em uma vírgula.