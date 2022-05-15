tabuada = int(input('Digite um número: '))

print('-=-'*20)
print('A tabuada do número {} é: '.format(tabuada))

print('-=-'*20)
for c in range(1, 11):
    print('{} x {} = {:.0f}'.format(tabuada, c, (tabuada*c)))
print('-=-'*20)