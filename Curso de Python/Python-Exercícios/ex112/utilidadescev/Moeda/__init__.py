def metade(n = 0, formato = False):
    res = n / 2
    return res if formato is False else moeda(res)
    #Vai retornar res(sem formatação) se o formato for false, se não, vai retornar o valor formatado.
    #O 'moeda(res)' é uma função do proprio modulo, se estivesse em outro local teria que importar.

def dobro(n = 0, formato = False):
    res = n * 2
    return res if formato is False else moeda(res)

def aumentar(n = 0, taxa = 0, formato = False):
    s = n + (n * taxa / 100)
    return s if formato is False else moeda(s)

def reduzir(n = 0, taxa = 0, formato = False):
    s = n - (n * taxa / 100) 
    return s if formato is False else moeda(s)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',') #Replace é para substituir, nesse caso vai substituir um ponto em uma vírgula.

def resumo(preco=0, taxa = 10, taxar = 5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'PREÇO ANALISADO: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Preço aumentado em {taxa}%: {aumentar(preco, taxa , True)}')
    print(f'Preço reduzido em {taxar}%: \t{reduzir(preco, taxar ,True)}')
    print('-'*30)

