nome=input('Digite o nome do funcionário: ')
empresa=input('Digite o nome da empresa: ')
qtdFuncionarios=int(input('Digite a quantidade de funcionários: '))
mediaMensalidade=float(input('Digite a média da mensalidade: '))

print(nome + ' trabalha na empresa ' + empresa)
print('possui: ', + qtdFuncionarios, ' funcionários.')
print('a media de mensalidade é de:  ' + str(mediaMensalidade))

print('========verifique os tipos de dados abaixo=========')
print('o tipo da variavel [nome] é: ',type(nome))
print('o tipo da variavel [empresa] é: ',type(empresa))
print('o tipo da variavel [qtdFuncionarios] é: ',type(qtdFuncionarios))
print('o tipo da variavel [mediaMensalidade] é: ',type(mediaMensalidade))