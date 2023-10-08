# Banco Alagoas V1
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
# Definimos o menu das possíveis ações que são realizadas. 
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

#definimos as variáveis e constatantes
while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("informe o valor de depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque>= LIMITE_SAQUE

        if excedeu_saldo:
            print("Saque não realizado! Saldo insufuciente. ")
        
        elif excedeu_limite:
            print("Saque não realizado! O valor digitado excede o limite permitido.")
        
        elif excedeu_saques:
            print("Não foi possível realizar a operação. O número máximo de saques diários já foi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é inválido")
        
    elif opcao == "e":
        print("\n=============== EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
        