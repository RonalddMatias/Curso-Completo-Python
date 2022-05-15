try: #Para tentar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): #Se der problema vai aparecer o print abaixo
    print(f'Tivemos um problema com os tipos de dados que você informou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por 0!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as error:
    print(f'O erro encontrado foi {error.__cause__}')
else: #Quando dar certo
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito Obrigado!')