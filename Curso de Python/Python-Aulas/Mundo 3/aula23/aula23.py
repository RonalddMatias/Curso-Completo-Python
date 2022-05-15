try: #Para tentar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: #Se der problema vai aparecer o print abaixo
    print(f'O problema encontado foi {erro.__class__}')
else: #Quando dar certo
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito Obrigado!')