def area():
    a = float(input('Largura (m): '))
    b = float(input('Comprimento (m): '))
    soma = a * b
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {soma:.1f}m² ')
def layout():
    print('-'*40)
    print('         CONTROLE DE TERRENOS         ')
    print('-'*40)

layout()
area()