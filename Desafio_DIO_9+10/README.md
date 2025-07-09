O arquivo Analisar_Veiculo.py é feito para Verificar a Antiguidade de um veiculo conforme adicionado os seus dados.
O objetivo deste desafio é criar uma classe Veiculo que armazena os dados de um carro e possui um método para determinar se ele é "antigo" ou "novo".

Implementação:
A classe Veiculo é inicializada com os atributos marca, modelo e ano.
O método verificar_antiguidade() calcula a idade do veículo subtraindo seu ano de fabricação do ano atual (obtido com a biblioteca datetime).
O método retorna "Veículo antigo" se a idade for superior a 20 anos, e "Veículo novo" caso contrário.

Ja o arquivo Calcular_Pedido.py como já está explicito no seu nome foi feito para calcular um pedido, usando listas e outros metodos.

Implementação:
A classe Pedido possui uma lista itens para armazenar os preços.
O método adicionar_item(preco) converte o preço para float e o adiciona à lista.
O método calcular_total() utiliza a função sum() para somar todos os valores da lista de forma eficiente.
A saída é formatada para exibir o valor total com exatamente duas casas decimais (ex: 47.50).
