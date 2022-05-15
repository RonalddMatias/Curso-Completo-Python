from traceback import print_tb


n1 = int(input('digite um número: '))
n2 = int(input('digite um número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma dos números é {},  o produto é {} e a divisão é {:.3f}'.format(
    s, m, s), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))
