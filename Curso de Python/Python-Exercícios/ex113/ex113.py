from funcoes import leiaFloat
from funcoes import leiaInt

num = leiaInt.leiaInt('Digite um inteiro: ')
n1 = leiaFloat.leiaFloat('Digite um Real: ')
print(f'\033[32mO valor digitado inteiro digitado foi {num:.0f} e o real foi {n1:.0f}!\033[m')
