import textwrap

# --- Funções Auxiliares (Helpers) para Reduzir Código ---

def solicitar_valor_numerico(prompt):
    """Solicita um número ao usuário e garante que a entrada seja válida."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            exibir_erro("Entrada inválida. Por favor, digite um número.")

def exibir_sucesso(mensagem):
    """Exibe uma mensagem de sucesso padronizada."""
    print(f"\n✅ {mensagem}")

def exibir_erro(mensagem):
    """Exibe uma mensagem de erro padronizada."""
    print(f"\n❌ {mensagem}")

# --- FUNÇÃO PRINCIPAL DA MELHORIA: O PAINEL COMPLETO ---

def exibir_painel_informativo(usuario, conta, saldo, limite, num_saques, limite_saques):
    """Exibe um painel completo com dados do cliente e status financeiro."""
    print("------------------ PAINEL DO CLIENTE -------------------")
    
    # Bloco de Identificação
    print("--- [ IDENTIFICAÇÃO ] --------------------------------")
    if not usuario:
        print("  Nenhum cliente ativo. Cadastre um usuário e conta.")
    else:
        print(f"  Cliente: {usuario['nome']}")
        if not conta:
            print("  Nenhuma conta ativa.")
        else:
            print(f"  Agência: {conta['agencia']} | C/C: {conta['numero_conta']}")
    
    # Bloco Financeiro
    print("--- [ STATUS FINANCEIRO ] ----------------------------")
    print(f"  💰 Saldo em Conta: R$ {saldo:.2f}")
    print(f"  🎯 Limite de Saque: R$ {limite:.2f}")
    print(f"  🔄 Saques Hoje: {num_saques}/{limite_saques}")
    print("------------------------------------------------------")


def menu():
    """Exibe o menu de opções para o usuário."""
    menu_texto = """
    ================ MENU DE OPÇÕES ================
    [d]  Depositar      [nu] Novo Usuário      [q] Sair
    [s]  Sacar          [lu] Listar Usuários
    [e]  Extrato        [nc] Nova Conta
    [v]  Ver Status     [lc] Listar Contas
    => """
    return input(textwrap.dedent(menu_texto)).lower()

# ... (As funções depositar, sacar, exibir_extrato, etc. permanecem as mesmas) ...
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        exibir_sucesso("Depósito realizado!")
    else:
        exibir_erro("O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        exibir_erro("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        exibir_erro("Operação falhou! Valor do saque excede o limite diário.")
    elif numero_saques >= limite_saques:
        exibir_erro("Operação falhou! Número máximo de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        exibir_sucesso("Saque realizado!")
        if numero_saques > 0 and numero_saques % 3 == 0:
            limite += 250
            print(f"\n✨ Parabéns! Seu limite diário aumentou para R$ {limite:.2f}! ✨")
    else:
        exibir_erro("O valor informado é inválido.")
    return saldo, extrato, numero_saques, limite

def exibir_extrato(saldo, /, *, extrato):
    print("\n============= EXTRATO BANCÁRIO =============")
    print("Nenhuma movimentação realizada." if not extrato else extrato)
    print(f"\nSaldo Atual: R$ {saldo:.2f}")
    print("============================================")

def exibir_status_conta(saldo, limite_saque, numero_saques, limite_saques_diarios):
    saques_restantes_bonus = 3 - (numero_saques % 3) if numero_saques % 3 != 0 else 0
    if numero_saques == 0: saques_restantes_bonus = 3
    print("\n================ STATUS DA CONTA ================")
    print(f"Saldo em conta: R$ {saldo:.2f}")
    print(f"Limite de saque diário: R$ {limite_saque:.2f}")
    print(f"Saques realizados hoje: {numero_saques} de {limite_saques_diarios}")
    print(f"Saques restantes para o bônus: {saques_restantes_bonus}")
    print("============================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        exibir_erro("Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    exibir_sucesso("Usuário criado!")

def listar_usuarios(usuarios):
    if not usuarios:
        print("\nNenhum usuário cadastrado.")
        return
    print("\n================ LISTA DE USUÁRIOS ================")
    for usuario in usuarios:
        info = f"""\
            Nome:\t{usuario['nome']} | CPF: {usuario['cpf']}
            Endereço: {usuario['endereco']}"""
        print(textwrap.dedent(info))
        print("-" * 50)

def filtrar_usuario(cpf, usuarios):
    return next((u for u in usuarios if u["cpf"] == cpf), None)

def criar_conta(agencia, numero_conta, usuarios):
    if not usuarios:
        exibir_erro("Nenhum usuário cadastrado. Crie um usuário primeiro.")
        return None
    cpf = input("Informe o CPF do usuário para vincular a conta: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        exibir_sucesso("Conta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    exibir_erro("Usuário não encontrado.")
    return None

def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    print("\n================= LISTA DE CONTAS =================")
    for conta in contas:
        linha = f"""\
            Titular:\t{conta['usuario']['nome']}
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}"""
        print("-" * 50)
        print(textwrap.dedent(linha))

def main():
    """Função principal que orquestra todo o sistema."""
    saldo, limite_saque_diario, extrato = 0, 500, ""
    numero_saques, LIMITE_SAQUES_DIARIOS = 0, 3
    AGENCIA, usuarios, contas = "0001", [], []

    while True:
        usuario_ativo = usuarios[-1] if usuarios else None
        conta_ativa = contas[-1] if contas else None
        
        # A chamada para o painel agora inclui os dados financeiros.
        exibir_painel_informativo(
            usuario_ativo, conta_ativa, saldo, 
            limite_saque_diario, numero_saques, LIMITE_SAQUES_DIARIOS
        )
        opcao = menu()

        # ... (O resto do loop main permanece o mesmo) ...
        if opcao == "d":
            valor = solicitar_valor_numerico("Informe o valor do depósito: R$ ")
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = solicitar_valor_numerico("Informe o valor do saque: R$ ")
            saldo, extrato, numero_saques, limite_saque_diario = sacar(
                saldo=saldo, valor=valor, extrato=extrato, limite=limite_saque_diario,
                numero_saques=numero_saques, limite_saques=LIMITE_SAQUES_DIARIOS,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "v":
            exibir_status_conta(saldo, limite_saque_diario, numero_saques, LIMITE_SAQUES_DIARIOS)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "lu":
            listar_usuarios(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("\nSaindo do sistema... Agradecemos a sua preferência!")
            break
        else:
            exibir_erro("Operação inválida. Por favor, selecione uma opção do menu.")

if __name__ == "__main__":
    main()