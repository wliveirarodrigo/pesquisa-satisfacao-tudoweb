#Pesquisa de satisfação: TudoWeb

#Variaveis começam com valor zero
excelente = 0
bom = 0
ruim = 0

#Estrutura de repetição valida para 50 repetições
for i in range(50):
    print('\nEntrevistado', i + 1)

    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))

    print('Opções de atendimento:')
    print('1 - EXCELENTE')
    print('2 - BOM')
    print('3 - RUIM')

    opiniao = int(input('Digite a opção: '))

#Verifica e armazena a opnião do usuario
    if opiniao == 1:
        excelente = excelente + 1
    elif opiniao == 2:
        bom = bom + 1
    elif opiniao == 3:
        ruim = ruim + 1
    else:
        #Informa ao usuario caso ele digite uma opção invalida
        print('Opção inválida.')

print('\n##### RESULTADO DA PESQUISA #####')
print('Quantidade de respostas EXCELENTE:', excelente)
print('Quantidade de respostas RUIM:', ruim)
