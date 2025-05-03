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
    D. Cadastrar Cliente
    E. Criar Conta
    F. Listar Contas
    G. Para Sair
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

def criar_cliente(clientes):
    cpf = input("Entre com seu CPF : ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nCliente já é cadastrado !! !!")
        return

    nome = input("Insira seu nome completo: ")
    data_nascimento = input("Qual a data de nascimento : ")
    endereco = input("Qual seu endereço : ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Qual o CPF do Cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n Conta criada com sucesso !!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("\nNão foi possível concluir !!!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saque = 3
    clientes = []
    contas = []
    agencia = "0001"
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

        elif opcao == "D":
            criar_cliente(clientes)

        elif opcao == "E":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, clientes)

            if conta:
                contas.append(conta)

        elif opcao == "F":
            listar_contas(contas)

        elif opcao == "G":
            break


        else:
                print("Opção inválida. Tente novamente.")

        continuar = input("\nDeseja continuar? (s/n): ").lower()


main()
