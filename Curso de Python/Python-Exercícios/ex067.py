while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*40)
    for c in range(0,11):
        print(f'{n} x {c} = {c*n}')
    print('-'*40)
print('FIM DO PROGRAMA DE TABUADA')