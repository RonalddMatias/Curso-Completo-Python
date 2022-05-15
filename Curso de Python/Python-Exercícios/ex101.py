def voto(ano):  # O que fica dentro do parêntese é o ano.
    # Importação local, só funciona dentro dessa função.
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota!'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Não obrigatório!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

n = int(input('Em que ano você nasceu? '))
m = (voto(n)) #O return me da a opção de botar o resultado em uma variável.
print(m)