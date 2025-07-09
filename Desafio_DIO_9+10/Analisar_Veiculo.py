from datetime import datetime

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def verificar_antiguidade(self):
        # Obtém o ano atual usando a biblioteca datetime
        ano_atual = datetime.now().year
        
        # Calcula a idade do veículo
        idade_do_veiculo = ano_atual - self.ano
        
        # Verifica se a idade é maior que 20 anos
        if idade_do_veiculo > 20:
            return "Veículo antigo"
        else:
            return "Veículo novo"

# Entrada direta dos dados do veículo
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto da classe Veiculo
veiculo = Veiculo(marca, modelo, ano)

# Chamando o método para verificar a antiguidade e imprimindo o resultado
print(veiculo.verificar_antiguidade())