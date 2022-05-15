print('=====DESAFIO 07=====')
nota_1 = float(input('Digite a sua primeira nota: '))
nota_2 = float(input('Digite a sua segunda nota: '))
media = (nota_1 + nota_2)/2
print(f'A sua média na disciplina foi: {media}')

if media < 7:
    print('\033[31mVocê foi reprovado nesta matéria.Sinto muito.\033[m')
else:
    print('\033[32mParabéns, você foi aprovado!\033[m')
