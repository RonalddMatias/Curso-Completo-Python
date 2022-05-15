def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip() #Substituir todas sas virgular por pontos e tirar todos os espaços
        if entrada.isalpha() or entrada == '': #se essa entrada é alpha numérico ou se, depois de tirar todos os espaços, a entrada está vazia, então:
            print(f'\033[31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)

#SE MISTURAR NUMERO E LETRA O PROGRAMA VAI DAR ERRO