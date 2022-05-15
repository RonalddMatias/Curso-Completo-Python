import math
print('====DESAFIO 18====')
ang = float(input('Digite um angulo da circunferência: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O angulo de {}° tem um seno de {:.2f}, um cosseno de {:.2f} e uma tangente de {:.2f}'.format(ang, sen, cos, tang))