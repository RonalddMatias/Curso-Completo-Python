n = 0
cont = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999: #interropendo o flag
        break
    s += n
print(f'a soma é {s}') #comando nobo, a famosa Fstring