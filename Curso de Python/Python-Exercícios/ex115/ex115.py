from time import sleep
from biblioteca import interfac
from biblioteca import arquivo


arq = 'ultimoexercicio.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interfac.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'sair do sistema'])
    if resposta == 1:
        #Opção de listar o conteudo de um arquivo
        arquivo.LerAquivo(arq)
    elif resposta == 2:
        #Opcao de cadastar uma nova pessoa.
        interfac.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = interfac.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        interfac.cabecalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO: digite uma opção válida\033[m')
    sleep(2)
