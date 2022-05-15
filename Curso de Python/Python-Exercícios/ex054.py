from datetime import date
cont = 0
con = 0
anoAtual = date.today().year
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if anoAtual - ano <18:
        cont += 1
    else:
        con += 1
print('{} pessoas são menores de idade \n{} são maiores de idade'.format(cont, con))
 

