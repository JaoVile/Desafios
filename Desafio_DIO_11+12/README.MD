Login_Simples.py
Objetivo: Validar credenciais de usuário (nome e senha) contra um conjunto de registros pré-definidos.

Implementação:

Utiliza um dicionário para armazenar pares de usuário e senha.
Uma instrução if verifica se o usuário existe como chave e se a senha fornecida corresponde ao valor associado.
Retorna "Acesso permitido" para credenciais corretas ou "Usuário ou senha incorretos" para inválidas.

2. Checar_Produtos.py
Objetivo: Verificar a disponibilidade de um produto em uma lista de estoque.

Implementação:

Utiliza uma lista para armazenar os nomes dos produtos em estoque.
O operador in é usado para checar eficientemente se o produto solicitado existe na lista.
Retorna "Produto disponível" se o item for encontrado ou "Produto esgotado" caso contrário.