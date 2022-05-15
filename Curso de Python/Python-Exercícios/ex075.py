n1 = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
      int(input('Digite o quarto número: ')), int(input('Digite o quinto número: ')))

print(f'Você digitou os números {n1}')
print(f'O valor nove apareceu {n1.count(9)} vezes')
if 3 in n1: #Se tiver 3 na tupla
    print(f'O número três foi digitado pela primeira vez na posição {n1.index(3)}ª')
else: #se não
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in n1:  # Para cada valor em número
    if n % 2 == 0: # vai testar valor por valor que esta em n1
        print(n, end=' ') #printar os valores que atederem as condições.
