def verificação(valor):
    if opção == 1:
        cpf = []
        cont = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        multiplicação = []
        multiplicação_2 = []
        if len(valor) != 11:
            return False
        elif valor.isnumeric() != True:
            return  False
        else:
            for val in valor:
                cpf.append(int(val))
            multiplicação = [x*y for x, y in zip(cpf[:9],cont[1:])]
            multiplicação_2 = [x*y for x, y in zip(cpf[:10],cont[:])]
            soma = sum(multiplicação)
            soma_2 = sum(multiplicação_2)
            result = soma % 11
            result_2 = soma_2 % 11
            if result <= 1:
                result = 0
            else:
                result = 11 - result
            if result_2 <= 1:
                result_2 = 0
            else:
                result_2 = 11 - result_2
            if result == cpf[9] and result_2 == cpf[-1]:
                return True
            else:
                return False
    if opção == 2:
        cnpj = []
        cont = [5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
        multiplicação_3 = []
        multiplicação_4 = []
        if len(valor) != 14:
            return False
        elif valor.isnumeric() != True:
            return  False
        else:
            for val in valor:
                cnpj.append(int(val))
            multiplicação_3 = [x*y for x, y in zip(cnpj[:12],cont[1:])]
            multiplicação_4 = [x*y for x, y in zip(cnpj[:13],cont[:])]
            soma_3 = sum(multiplicação_3)
            soma_4 = sum(multiplicação_4)
            result3 = soma_3 % 11
            result_4 = soma_4 % 11
            penultimo_ok = False
            ultimo_ok = False
            if result3 >= 10:
                result3 = 0
                if result3 == cnpj[12]:
                    penultimo_ok = True
                else:
                    return False
            else:
                if result3 == cnpj[12]:
                    penultimo_ok = True
                else:
                    return False
            if result_4 >= 10:
                result_4 = 0
                if result_4 == cnpj[-1]:
                    ultimo_ok = True
                else:
                    return False
            else:
                if result_4 == cnpj[-1]:
                    ultimo_ok = True
                else:
                    return False
            if penultimo_ok and ultimo_ok:
                return True
            else:
                return False

while True:
    print("""
Selecione uma das opção a seguir:

[ 1 ] Validar CPF
[ 2 ] Validar CNPJ
[ 3 ] Imprimir o menu novamente
[ 0 ] Sair
""")
    opção = (int(input('Opção -> ')))

    if opção == 1:
        while True:
            if verificação(input('Digite seu CPF -> ')) == True:
                print('Seu CPF é Válido.')
                escolha = input('Voltar para o menu? [S/N]: ').strip().upper()[0]
                if escolha == 'S':
                    opção == 3
                    break
                else:
                    pass
            else:
                print('Seu CPF Não é Valido ou foi digitado incorretamente.')
                continue

    if opção == 2:
        while True:
            if verificação(input('Digite seu CNPJ -> ')) == True:
                print('Seu CNPJ é Válido.')
                escolha = input('Voltar para o menu? [S/N]: ').strip().upper()[0]
                if escolha == 'S':
                    opção == 3
                    break
                else:
                    pass
            else:
                print('Seu CNPJ Não é Valido ou foi digitado incorretamente.')
                continue

    if opção == 3:
        continue

    if opção == 0:
        print('Encerrando..')
        break
