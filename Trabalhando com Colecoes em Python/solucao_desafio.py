menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[cu] Criar usuário
[nc] Nova Conta
[p] ver usuários
[q] Sair

=> """

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Caixa R$ {valor:.2f}\n"
        print("O depósito foi realizado com sucesso.")

    else:
        print("Você digitou um valor inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
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
        print("O saque foi realizado com sucesso.")

    else:
        print("O valor digitado é inválido.")

    return saldo, extrato

def ver_extrato(saldo, /, *, extrato):
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(f"Valor em caixa R$ {saldo:.2f}.")

def achar_usuario(cpf, usuarios):
    filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtro[0] if filtro else None

def criar_usuario(usuarios):
    cpf = input("Digite o cpf do usuario (apenas números): ")
    usuario = achar_usuario(cpf, usuarios)

    if usuario:
        print("Existe um usuário com esse cpf registrado.")
        return
    
    nome = input("Digite seu nome: ")
    nascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    print("Usuário registrado com sucesso.")

    usuarios.append({"nome":nome, "nascimento":nascimento, "cpf": cpf, "endereco":endereco})

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o cpf do usuário: ")
    usuario = achar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    #else:
    print("usuario não encontrado, não foi possivel criar conta.")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []
numero_conta = 1

while True:

    digito = input(menu)

    if digito == "d":
        valor = float(input("Digite o valor que deseja depositar: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif digito == "s":
        valor = float(input("Digite o valor do saque: "))
        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite,numero_saques=numero_saques,LIMITE_SAQUES=LIMITE_SAQUES,)

    elif digito == "e":
        ver_extrato(saldo, extrato=extrato)

    elif digito == "cu":
            criar_usuario(usuarios)

    elif digito == "nc":
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
            numero_conta += 1

    elif digito == "p":
         print(usuarios)

    elif digito == "q":
        break

    else:
        print("Operação inválida, digite outra operação.")