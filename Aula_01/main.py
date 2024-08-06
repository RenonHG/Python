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

'''
01- Atividade
    O sistema deve solicitar o número ao usuario
    O sistema deve percorrer do 0 até o número escolhido 🆗
    Se o numero for menor ou igual do 0 peça que o usuário digite novamente até receber um número valido 🆗
    No laço se o número for PAR deve ficar em AZUL e se for IMPAR deve ficar em VERMELHO

'''
# numero = input('Digite um número maior que 0: ')
numero = '0'

while numero < '1':
    numero = input('Digite um número maior que 0: ')


for i in range(0, int(numero)+1):
    if i % 2 == 0:
        print('\033[34m' + str(i))
    else:
        print('\033[31m' + str(i))

