class Pedido:
    def __init__(self):
        self.itens = []  
    
    def adicionar_item(self, preco):
        self.itens.append(float(preco))

    def calcular_total(self):
        return sum(self.itens)

# Lê a quantidade de itens do pedido
quantidade_pedidos = int(input().strip())

# Cria uma instância da classe Pedido
pedido = Pedido()

# Loop para ler cada item e adicioná-lo ao pedido
for _ in range(quantidade_pedidos):
    entrada = input().strip()
    # Separa o nome do preço (que vem como string)
    nome, preco = entrada.rsplit(" ", 1)
    #TODO: Chame o método adicionar_item corretamente: 
    pedido.adicionar_item(preco)

# TODO: Exiba o total formatado com duas casas decimais:
total_calculado = pedido.calcular_total()
print(f"{total_calculado:.2f}")
