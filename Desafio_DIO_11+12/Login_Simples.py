# Dicionário com usuários cadastrados e suas senhas
usuarios = {
    "joao": "1234",
    "ana": "abcd",
    "maria": "senha123",
    "marcelo": "iou789",
}

# Entrada do usuário
usuario = input().strip()
senha = input().strip()

# TODO: Verifique se o usuário existe e a senha está correta:
# 1. Verifica se o 'usuario' (a chave) existe no dicionário 'usuarios'
# 2. Se existir, verifica se a senha fornecida é igual ao valor correspondente à chave
if usuario in usuarios and usuarios[usuario] == senha:
    print("Acesso permitido")
else:
    print("Usuário ou senha incorretos")
