menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    digito = input(menu)

    if digito == "d":
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Caixa R$ {valor:.2f}\n"

        else:
            print("Você digitou um valor inválido.")

    elif digito == "s":
        valor = float(input("Digite o valor do saque: "))

        if valor > saldo:
            print("Você não tem saldo para realizar esse saque.")

        elif valor > limite:
            print("O valor máximo de saque por operação é R$500, tente novamente com um valor menor.")

        elif numero_saques >= LIMITE_SAQUES:
            print("O valor máximo de saques diários foi ultrapassado.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Caixa R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor digitado é inválido.")

    elif digito == "e":
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(f"Saldo R$ {saldo:.2f}")

    elif digito == "q":
        break

    else:
        print("Operação inválida, digite outra operação.")