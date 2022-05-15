def metade(n = 0):
    return n / 2

def dobro(n = 0):
    return n * 2

def aumentar(n = 0):
    s = n * 1.1
    return s #aumentar 10%

def reduzir(n = 0):
    s = n * 0.87 #diminuir 13%
    return s

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',') #Replace é para substituir, nesse caso vai substituir um ponto em uma vírgula.