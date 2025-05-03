import textwrap


def menu():
    menu = """
    ------------------------------------------------
    **************************************************
            Bem-vindo ao Banco QUEBRADO!
    **************************************************
            Operações disponíveis:

    A. Depositar
    B. Sacar
    C. Extrato
    -------------------------------------------------
    """

    return input(textwrap.dedent(menu))


def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        print(f"Saldo atual = {saldo}")
    else:
        print("\nValor inválido para depósito.")
    return saldo, extrato


def sacar(saldo, valor, extrato, numero_saques, limite, limite_saque):
    if valor > (saldo + limite):
        print("\nSaldo insuficiente.")
    elif numero_saques >= limite_saque:
        print("\nNúmero máximo de saques atingido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
        print(f"Saldo atual = {saldo}")
        print(f"Saques realizados : {numero_saques}")
    return saldo, extrato, numero_saques


def exibe_extrato(extrato, saldo, numero_saques):
    print("\n==================== Extrato ====================")
    print(extrato if extrato else "Nenhuma movimentação realizada.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print(f"Saques realizados = {numero_saques}")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saque = 3
    continuar = "s"

    while (continuar != "n"):

        opcao = menu().strip().upper()

        if opcao == "A":
            valor = float(input("\nDigite o valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == "B":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, numero_saques, limite, limite_saque)

        elif opcao == "C":
            exibe_extrato(extrato, saldo, numero_saques)


        else:
            print("Opção inválida. Tente novamente.")
        continuar = input("\nDeseja continuar? (s/n): ").lower()


main()
