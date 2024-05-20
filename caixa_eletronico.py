import textwrap
import time

time.sleep(0.1)

def menu():
    menu = """\n
    ================ OPERAÇÕES ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        time.sleep(0.3)
        print("\n=== Depósito efetuado! ===")
        time.sleep(1.5)
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        time.sleep(2)

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        time.sleep(2)

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor disponível por saque é de R$500.00 @@@")
        time.sleep(2)

    elif excedeu_saques:
        print("\n@@@ Operação falhou! O limite diário de saques (3) foi atingido. @@@")
        time.sleep(2)

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
        time.sleep(1.5)

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        time.sleep(2)

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações na sua conta." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")
    time.sleep(4)


def criar_usuario(usuarios):
    time.sleep(0.1)
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    time.sleep(2)

    nome = input("Informe o nome completo: ")
    time.sleep(0.1)
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    time.sleep(0.1)
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")
    time.sleep(1.5)


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        time.sleep(1.5)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    time.sleep(2)


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        time.sleep(4)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            time.sleep(0.3)
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            time.sleep(0.3)
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            time.sleep(0.3)
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            time.sleep(0.3)
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            time.sleep(0.3)
            listar_contas(contas)

        elif opcao == "6":
            time.sleep(0.3)
            criar_usuario(usuarios)

        elif opcao == "0":
            print("Finalizando...")
            time.sleep(1)
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada ou encerre o programa.")


main()