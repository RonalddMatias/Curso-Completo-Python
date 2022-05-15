from datetime import date 

print('\033[33m-=-\033[m' * 50)
print(f'{"ALISTAMENTO MILITAR":^140}')
print('\033[33m-=-\033[m' * 50)

genero = str(input('Digite seu gênero: ')).strip().lower()
atual = date.today().year
anoNasc = int(input('\nDigite seu ano de nascimento: '))
idade = date.today().year - anoNasc

print('Quem nasceu em {} tem {} anos em {}.'.format(anoNasc, idade, atual))

if genero == 'feminino':
    print('Você não é obrigada a se alistar no Exercito Brasileiro!')
elif genero == 'masculino' and idade == 18:
    print('Você é obrigado a se alistar no Exército Brasileiro')
    print('\033[32mVocê já tem {} anos, chegou a hora de servir a pátria!\033[m'.format(idade))
elif idade < 18:
    print('\033[31mVocê ainda não tem a idade necessária pra ingressar no Exercito Brasileiro.\033[m')
    print('\033[31mFalta {} anos para você servir a pátria.\033[m'.format(18-idade))
else:
    print('\033[33mVocê ja tem a idade necessária para servir ao Exercito Brasileiro. \nProcure o mais rápido possível uma junta de Serviço Militar!\033[m')
    print('\033[33mJá se passaram {} anos do seu alistamento.\033[m'.format(idade-18))
    print('\033[33mSeu alistamento deveria ter sido no ano de {}.\033[m'.format(anoNasc + 18))





'''if idade < 18:
    print('\033[31mVocê ainda não tem a idade necessária pra ingressar no Exercito Brasileiro.\033[m')
    print('\033[31mFalta {} anos para você servir a pátria.\033[m'.format(18-idade))
elif idade == 18:
    print('\033[32mVocê já tem {} anos, chegou a hora de servir a pátria!\033[m'.format(idade))
else:
    print('\033[33mVocê ja tem a idade necessária para servir ao Exercito Brasileiro. \nProcure o mais rápido possível uma junta de Serviço Militar!\033[m')
    print('\033[33mJá se passaram {} anos do seu alistamento.\033[m'.format(idade-18))
    print('\033[33mSeu alistamento deveria ter sido no ano de {}.\033[m'.format(anoNasc + 18))
'''
