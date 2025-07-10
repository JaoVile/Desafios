# Lista de produtos disponíveis no estoque
estoque = ["Camiseta", "Calça", "Tênis", "Boné", "Jaqueta"]

# Entrada do usuário
produto = input().strip()

# TODO: Verifique se o produto está no estoque:
# A palavra-chave 'in' verifica se um item existe dentro de uma lista (ou outra sequência).
if produto in estoque:
    # Se o produto for encontrado na lista 'estoque', esta mensagem é exibida.
    print("Produto disponível")
else:
    # Caso contrário, se o produto não estiver na lista, esta mensagem é exibida.
    print("Produto esgotado")
