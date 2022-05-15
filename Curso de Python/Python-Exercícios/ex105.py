from tkinter import N


def notas(*num, sit=False):
    r = {}  # dicionário
    r['total'] = len(num)  # Key e Chave
    r['Maior'] = max(num)  # Key e Chave
    r['Menor'] = min(num)  # Key e Chave
    r['Média'] = sum(num)/len(num) # Soma todos os valores e divide pela qtd de termos
    if sit == True:
        if r['Média'] > 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(5.5, 9.0, 8.0, sit=True)
print(resp)
