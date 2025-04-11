menu = """
========== MENU ==========
1 - Depositar
2 - Sacar
3 - Extrato
0 - Sair

Digite uma opção: """

saldo = 0
limite = 500
extrato = [] 
numero_saques = 0
limite_saques = 3

while True:
    try:
        opcao = int(input(menu))
    except ValueError:
        print('\nOpção inválida. Por favor, insira uma opção válida.')
        continue

    if opcao == 1:  # Depositar
        try:
            valor = float(input('\nInforme o valor do depósito: '))
        except ValueError:
            print('\nValor inválido. Por favor, repita a operação com um valor válido.')
            continue

        if valor > 0:
            saldo += valor
            extrato.append({'tipo': 'Depósito', 'valor': valor})
            print('\nDepósito realizado com sucesso.')

        else:
            print('\nValor inválido. Por favor, repita a operação com um valor válido.')


    elif opcao == 2:  # Sacar
        if numero_saques < limite_saques:

            try:
              valor = float(input('\nInforme o valor do saque: '))
            except ValueError:
                print('\nValor inválido. Por favor, repita a operação com um valor válido.')
                continue

            if valor > 0 and valor <= limite and valor <= saldo:
                saldo -= valor
                extrato.append({'tipo': 'Saque', 'valor': valor})
                numero_saques += 1
                print('\nSaque realizado com sucesso.')

            elif valor > saldo:
                print('\nSaldo insuficiente. Consulte seu extrato para verificar seu saldo.')

            elif valor > limite:
                print('\nValor do saque maior que limite diário. Por favor, repita a operação.')

            else:
                print('\nValor inválido. Por favor, repita a operação com um valor válido.')
        
        else:
            print('\nLimite de saque diário já atingido. Saque não permitido.')


    elif opcao == 3:  # Extrato
        if not extrato:  # Verifica se o extrato está vazio
            print('\n************* EXTRATO *************')
            print('Não foram realizadas movimentações.')
            print(f"\nSaldo atual: R$ {saldo:>9.2f}")
            print('***********************************')

        else:
            print('\n******** EXTRATO ********')
            for operacao in extrato:
                print(f"{operacao['tipo']:<11}: R$ {operacao['valor']:>9.2f}")
            print(f"\nSaldo atual: R$ {saldo:>9.2f}")
            print('*************************')

            
    elif opcao == 0:  # Sair
        print('\nOperação finalizada.')
        break


    else:  # Caso o número não seja uma opção válida
        print('\nOpção inválida. Tente novamente.')