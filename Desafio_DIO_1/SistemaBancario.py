# Desafio de Projeto: Criando um Sistema Bancário
# Autor: JaoVile

# --- Configurações Iniciais ---
saldo = 0
limite_saque_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

# --- Menu de Operações ---
menu = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[v] Ver Status da Conta
[q] Sair
======================================
=> """

# --- Loop Principal ---
while True:
    opcao = input(menu).lower()

    # [d] Operação de Depósito
    if opcao == "d":
        print("--- Depósito ---")
        valor = float(input("Informe o valor a ser depositado: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    # [s] Operação de Saque
    elif opcao == "s":
        print("--- Saque ---")
        valor = float(input("Informe o valor a ser sacado: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque_diario
        excedeu_saques = numero_saques >= LIMITE_SAQUES_DIARIOS

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! Valor do saque excede o limite diário.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

            # Lógica de bônus por saques
            if numero_saques > 0 and numero_saques % 3 == 0:
                limite_saque_diario += 250
                print(f"Parabéns! Você atingiu {numero_saques} saques e seu limite diário aumentou para R$ {limite_saque_diario:.2f}!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    # [e] Operação de Extrato
    elif opcao == "e":
        print("\n============= EXTRATO BANCÁRIO =============")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        print("============================================")

    # [v] Ver Status da Conta
    elif opcao == "v":
        saques_restantes_para_bonus = 3 - (numero_saques % 3)
        if saques_restantes_para_bonus == 3 and numero_saques > 0:
            saques_restantes_para_bonus = 3
        elif numero_saques == 0:
             saques_restantes_para_bonus = 3

        print("\n================ STATUS DA CONTA ================")
        print(f"Saldo em conta: R$ {saldo:.2f}")
        print(f"Limite de saque diário: R$ {limite_saque_diario:.2f}")
        print(f"Saques realizados hoje: {numero_saques} de {LIMITE_SAQUES_DIARIOS}")
        print(f"Saques restantes para o próximo bônus de limite: {saques_restantes_para_bonus}")
        print("============================================")

    # [q] Sair do Sistema
    elif opcao == "q":
        print("Saindo do sistema... Agradecemos a sua preferência!")
        break

    # Opção Inválida
    else:
        print("Operação inválida. Por favor, selecione uma das opções do menu.")
