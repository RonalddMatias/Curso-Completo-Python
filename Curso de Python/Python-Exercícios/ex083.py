expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr: #para cada símbolo na expressão
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else: 
    print('Expressão Inválida')