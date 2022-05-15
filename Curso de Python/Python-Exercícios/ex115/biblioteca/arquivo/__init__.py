from biblioteca import interfac

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #Verificando se existe o aquivo txt
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #Adicionando o arquivo txt
        a.close
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def LerAquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        interfac.cabecalho('PESSOAS CADASTRADAS')
        for linha in a: #Para cada linha que está dentro do arquivo(a).
            dado = linha.split(';')
            dado[1] = dado[1].replace( '\n', '')
            print(f'{dado[0]:<30}  {dado[1]:>3} anos')

    finally:
        a.close() #fechar o arquivo.


def cadastrar(arq, nome ='desconhecido', idade = 0): #Dois parametro opcionais
    try:
        a = open(arq, 'at+') #Adicionar mais dados no arquivo
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')#Escrever dentro do arquivo
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()