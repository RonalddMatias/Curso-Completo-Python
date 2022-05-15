def fatorial(n, show=False):
    """
    -->Calcular o fatorial de um número
    n: Número a ser calculado.
    Show: Opcional de quiser mostrar a conta.
    """
    f = 1  # Não pode ser zero pq todo número multiplicado por zero é igual a zero.
    for c in range(n, 0, -1):  # Do número até o zero voltando de 1 em 1.
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
print(fatorial(6, show=False))
help(fatorial)