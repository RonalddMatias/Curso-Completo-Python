nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1+nota2) / 2

if media < 5: 
    print('A sua media foi {:.1f} \nVocê foi reprovado.'.format(media))
elif media > 5 and media <7:
    print('A sua média foi {:.1f} \nVocê vai para a recuperação'.format(media))
else:
    print('A sua média foi {:.1f}\nParabéns, você foi aprovado.'.format(media))