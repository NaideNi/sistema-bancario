import time

LIMITE_SAQUE = 3
saldo = 0
limite = 500
numero_saque = 0
extrato = ""

menu = """
=========== Olá! Selecione a operação a ser feita ===========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair 

=> """

while True:
    option = input(menu)

    if option == "d":
        time.sleep(0.3)
        value = float(input("Digite o valor do depósito: "))
        if value > 0:
            saldo += value
            extrato += f"Depósito R$ {value:.2f}\n"
            time.sleep(0.3)
            print("Depósito efetuado.")
            time.sleep(0.5)
        else:
            print("O valor informado é inválido.")
            time.sleep(0.8)

    elif option == "s":
        time.sleep(0.3)
        value = float(input("Valor do saque: "))
        # Checando o saldo disponível para saque
        saldo_disponivel = min(limite, saldo)
        print(f"Saldo disponível para saque: RS{saldo_disponivel:.2f}")
        time.sleep(1)

        ultrapassa_saque    = numero_saque >= LIMITE_SAQUE
        ultrapassa_limite   = value > limite
        ultrapassa_saldo    = value > saldo
        if ultrapassa_saque:
            print("O limite diário de saques (3) foi atingido.")
            time.sleep(3)
        elif ultrapassa_limite:
            print("Error: O valor disponível por saque é de R$500.00")
            time.sleep(3)
        elif ultrapassa_saldo:
            print("Você não tem saldo suficiente.")
            time.sleep(3)
        elif value > 0:
            saldo -= value
            extrato += f"Saque: R$ {value:.2f}\n"
            numero_saque += 1
        else:
            print("O valor informado é inválido.")
            time.sleep(3)

    elif option == "e":
        print("=========== Extrato ===========")
        print("Não foram realizadas movimentações na sua conta." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}\n")
        time.sleep(5)
        
    elif option == "q":
        print("Finalizando...")
        time.sleep(1.1)
        break
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada ou encerre o programa caso não deseje fazer operações")
        time.sleep(3)