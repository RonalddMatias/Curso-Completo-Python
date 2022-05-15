import random
print('\033[-=-\033[m'*20)
print(f"\033[33m{'JOGO DA ADVINHAÇÃO' : ^60}\033[m")
print('\033[-=-\033[m'*20)
print('Acabei de pensar em um número entre 0 e 10.')
print('Advinhe o número e ganhe um super prêmio!.')

palpite = int(input('E então, em qual numero você pensou? '))
tentativa = 1
numSecreto = random.randint(0, 10)
while palpite != numSecreto:
    tentativa += 1
    if palpite > numSecreto:
        print('\033[31mMenos... O número secreto está abaixo de {}\033[m'.format(palpite))
        palpite = int(input('E então, em qual numero você pensou?'))
    else:
        print('\033[31mMais... O número secreto está acima de {}\033[m'.format(palpite))
        palpite = int(input('E então, em qual numero você pensou?'))

print('\033[32mParabéns, você acertou!\033[32m')
print('\033[32mVocê tentou {} vezes para ganhar um beijo de Ronaldd\033[m'.format(tentativa))
