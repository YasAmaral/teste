menu = """ 
[d] deposito 
[s] saque 
[e] extrato 
[p] sair 

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"
        else:
            print("operação falhou, valor informado inválido")
    
    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
    
        if excedeu_saldo:
            print("operação falhou, está sem saldo")
        elif excedeu_limite:
            print("falha na operação, excedeu o limite")
        elif excedeu_saques:
            print("falha na operação, número máximo de saques excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("operação falhou! valor informado inválido")

    elif opcao == "e":
        print("\n=============Extrato=============")
        print("não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
    
    elif opcao == "p":
        break

    else:
        print("operação inválida, por favor selecione novamente a opção desejada")