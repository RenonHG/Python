"""
A proposta das aulas será desenvolver um campo minado

Básico de python
"""
print('''\033[35m
      
██████  ██    ██ ████████ ██   ██  ██████  ███    ██ 
██   ██  ██  ██     ██    ██   ██ ██    ██ ████   ██ 
██████    ████      ██    ███████ ██    ██ ██ ██  ██ 
██         ██       ██    ██   ██ ██    ██ ██  ██ ██ 
██         ██       ██    ██   ██  ██████  ██   ████ 
                                                     
\033[0;0m''')



# print('Bem vindo ao sistema malvadão: ')
# # numero1 = input('Digite um número: ')
# nome = 'Renon'
# idade = 18
# endereco = 'rua dos bobos'
# numero = 0
# telefone = '19 99999-9999'

# 'Dados cadastrados com sucesso'

# # print("\nCaro Sr. " + nome + " com a idade de " + idade + " anos, " +
# #  "residente na " + endereco + ", " + numero + ". Telefone: " + telefone)

# print("\nCaro Sr. {} com a idade de  {} anos, residente na {}, Nº {}. Telefone: {}"
#       .format(nome, idade, endereco, numero, telefone))
# #---------------------------------------------

# # Estrutura do IF, ELIF e ELSE
# if idade >= 18:
#     print('Você é maior de idade')
# elif idade < 10:
#     print('Você tem menos de 10 anos')
# else:
#     print('Você NÃO é maior de idade nem menor que 10 anos!')
# #---------------------------------------------

# # Estrutura do in
# vogal = ['a', 'e', 'i', 'o', 'u']

# if 'i' in vogal:
#     print('é vogal!')
# else:
#     print('Não é vogal!')
# #---------------------------------------------

# # Estrutura do For
# for i in range(1, 6):
#     print(str(i) + '- Calma calabreso!')

# # for e in juntos para listar cada letra na string
# for letra in '- Calma calabreso!':
#     print(letra)

# # for e in juntos para listar cada letra na vogal
# for letra in vogal:
#     print(letra)

#----------------------------------------------

# '''
# 01- Atividade
#     O sistema deve solicitar o número ao usuario
#     O sistema deve percorrer do 0 até o número escolhido 🆗
#     Se o numero for menor ou igual do 0 peça que o usuário digite novamente até receber um número valido 🆗
#     No laço se o número for PAR deve ficar em AZUL e se for IMPAR deve ficar em VERMELHO

# '''
# # numero = input('Digite um número maior que 0: ')
# numero = '0'

# while numero < '1':
#     numero = input('Digite um número maior que 0: ')


# for i in range(0, int(numero)+1):
#     if i % 2 == 0:
#         print('\033[34m' + str(i))
#     else:
#         print('\033[31m' + str(i))
# ---------------------------------------------


'''
02 - Atividade
    -Solicitar ao usuário um digito 🆗
    - Deve apresentar a quantidade em * na tela 🆗
    - solicitar 2º número 🆗
    - deve ser a quantidade de linhas apresentadas na tela 🆗
    
    - Crie o menu de acesso do jogo com as seguites opções: Jogar, Configurar e Sair 🆗
    - Hoje a gente vai criar o configurar, dê as opções ao usuário para ele configurar o jogo dele
    - Nessas configurações coloque uma terceira config "dificuldade", o usuário vai poder escolher  entre 1 e 3

'''
from openpyxl import Workbook, load_workbook
import random
 

def configs():
    try:
        wb = load_workbook(filename='campo.xlsx')
        config = wb['config']
        
    except:
        #criando tabela 
        wb = Workbook()
        config = wb.create_sheet('config')
        config.cell(column=1, row=1, value="linha")
        config.cell(column=2, row=1, value=5)
        config.cell(column=1, row=2, value="coluna")
        config.cell(column=2, row=2, value=5)
        config.cell(column=1, row=3, value="dificuldade")
        config.cell(column=2, row=3, value=2)


    linhas = config.cell(column=2, row=1).value
    colunas = config.cell(column=2, row=2).value
    dificuldade = config.cell(column=2, row=3).value



    wb.save('campo.xlsx')

    config = {
        'linhas' : int(linhas),
        'colunas' : int(colunas),
        'dificuldade' : int(dificuldade)
    }



    return config

def criarTabuleiro(qtdLinha, qtdColuna):
    print('- - - ' * int(qtdColuna))
    for i in range(0, int(qtdLinha)):
        for j in range(0, int(qtdColuna)):
            print('{:5}' . format('[   ]'), end=' ')
        print()
        print('- - - ' * int(qtdColuna))
        
def configCampo():
    novaQtdColuna = input('Quntas Colunas : ')
    novaQtdLinha = input('Quntas Linhas : ')
    novaDificuldade = input('1- Fácil \n2- Médio \n3- Difícil \n\nEscolha a dificuldade: ')

    try:
        wb = load_workbook(filename='campo.xlsx')
        config = wb['config']
    except:
        wb = Workbook()
        config = wb.create_sheet('config')

    config.cell(column=1, row=1, value="linha")
    config.cell(column=2, row=1, value=novaQtdLinha)
    config.cell(column=1, row=2, value="coluna")
    config.cell(column=2, row=2, value=novaQtdColuna)
    config.cell(column=1, row=3, value="dificuldade")
    config.cell(column=2, row=3, value=novaDificuldade)

    wb.save('campo.xlsx')

def calculoBombas():
    '''
    Descubra o valor total de 'casas' no tabuleiro, e a partir desse total calcule a quantidade de bombas que vai ter no tabuleiro;
    fácil → 15%, médio → 30% e díficil → 50%. 
    '''
    config = configs()
    totalCasas = config['linhas'] * config['colunas']

    
    if config['dificuldade'] == 1:
        quantBomba = totalCasas * 0.15

    if config['dificuldade'] == 2:
        quantBomba = totalCasas * 0.30

    if config['dificuldade'] == 3:
        quantBomba = totalCasas * 0.50

    print('Total de bombas: {}' .format(int(quantBomba)))

    
    

    # print(random.randint(1, 10))



    return int(quantBomba)
#==========================================================================

# config = configs()
# criarTabuleiro(config['linhas'], config['colunas'])
calculoBombas()

# while True:
#     #MENU DE SELEÇÃO
#     print('1 - JOGAR \n2 - CONFIGURAR \n3 - SAIR')
    
#     opcao = input('Escolha uma opção: ')

#     if opcao == '1':
#         print('JOGAR')

#     elif opcao == '2':
#         print('CONFIGURAR')
#         configCampo()
#         config = configs()
#         criarTabuleiro(config['linhas'], config['colunas'])
        
#     elif opcao == '3':
#         print('Sair')
#         break
                
#     else:
#         print('Selecione uma opção válida!')


