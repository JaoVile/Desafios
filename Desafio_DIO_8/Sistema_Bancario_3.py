import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

# --- Classes de Domínio ---

class Cliente:
    """Classe para representar um cliente do banco."""
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        """Realiza uma transação em uma conta específica."""
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """Adiciona uma conta para o cliente."""
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """Classe para representar um cliente do tipo Pessoa Física."""
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    """Classe base para todas as contas."""
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        """Método de fábrica para criar uma nova conta."""
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        """Saca um valor da conta."""
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n❌ Operação falhou! Saldo insuficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("\n✅ Saque realizado com sucesso!")
            return True
        else:
            print("\n❌ Operação falhou! O valor informado é inválido.")
        
        return False

    def depositar(self, valor):
        """Deposita um valor na conta."""
        if valor > 0:
            self._saldo += valor
            print("\n✅ Depósito realizado com sucesso!")
            return True
        else:
            print("\n❌ Operação falhou! O valor informado é inválido.")
            return False


class ContaCorrente(Conta):
    """Classe para representar uma Conta Corrente, com regras específicas."""
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        """Sobrescreve o método sacar para incluir regras da conta corrente."""
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.limite_saques

        if excedeu_limite:
            print(f"\n❌ Operação falhou! Valor do saque (R$ {valor:.2f}) excede o limite de R$ {self.limite:.2f}.")
        elif excedeu_saques:
            print("\n❌ Operação falhou! Número máximo de saques diários atingido.")
        else:
            # Chama o método sacar da classe pai (Conta)
            sucesso = super().sacar(valor)
            if sucesso:
                self.numero_saques += 1
                return True
        
        return False


class Historico:
    """Classe para gerenciar o histórico de transações."""
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """Adiciona uma nova transação ao histórico."""
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    """Classe abstrata para todas as transações."""
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    """Classe para representar uma transação de saque."""
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    """Classe para representar uma transação de depósito."""
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


# --- Funções de Interação com o Usuário ---

def menu():
    """Exibe o menu de opções para o usuário."""
    menu_texto = """
    ================ MENU DE OPÇÕES ================
    [d]  Depositar      [nu] Novo Usuário
    [s]  Sacar          [nc] Nova Conta
    [e]  Extrato        [lc] Listar Contas
    [q]  Sair
    => """
    return input(textwrap.dedent(menu_texto)).lower()

def filtrar_cliente(cpf, clientes):
    """Filtra um cliente na lista pelo CPF."""
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    """Recupera a conta de um cliente (considera apenas uma conta por simplicidade)."""
    if not cliente.contas:
        print("\n❌ Cliente não possui conta!")
        return None
    return cliente.contas[0]

def depositar(clientes):
    """Função para orquestrar a operação de depósito."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n❌ Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    """Função para orquestrar a operação de saque."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n❌ Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    """Função para orquestrar a exibição do extrato."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n❌ Cliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n============= EXTRATO BANCÁRIO =============")
    transacoes = conta.historico.transacoes
    extrato = ""
    if not transacoes:
        extrato = "Nenhuma movimentação realizada."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\t\tR$ {transacao['valor']:.2f}"
    
    print(extrato)
    print(f"\nSaldo Atual:\t\tR$ {conta.saldo:.2f}")
    print("============================================")

def criar_cliente(clientes):
    """Função para orquestrar a criação de um novo cliente."""
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("\n❌ Já existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("\n✅ Cliente criado com sucesso!")

def criar_conta(numero_conta, clientes, contas):
    """Função para orquestrar a criação de uma nova conta."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n❌ Cliente não encontrado, fluxo de criação de conta encerrado!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("\n✅ Conta criada com sucesso!")

def listar_contas(contas):
    """Função para listar todas as contas cadastradas."""
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    print("\n================= LISTA DE CONTAS =================")
    for conta in contas:
        print("-" * 50)
        print(textwrap.dedent(str(conta)))

# --- Função Principal ---

def main():
    """Função principal que orquestra todo o sistema."""
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("\nSaindo do sistema... Agradecemos a sua preferência!")
            break
        else:
            print("\n❌ Operação inválida. Por favor, selecione uma opção do menu.")


if __name__ == "__main__":
    main()