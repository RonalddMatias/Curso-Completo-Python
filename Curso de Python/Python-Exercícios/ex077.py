palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis',
            'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')
for p in palavras:  # Para cada palavra in palavras
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:  # para cada letra na palavra 
        if letra.lower() in 'aeiou': 
            print(letra, end=' ')
