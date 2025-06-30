def validar_email(email):
    """
    Verifica se um e-mail está em um formato válido.

    Regras:
    - Deve conter "@" e um domínio (ex: gmail.com, outlook.com).
    - Não pode começar ou terminar com "@".
    - Não pode conter espaços.
    """

    # 1. Verificar se o e-mail contém "@" e um domínio
    if "@" not in email:
        return "E-mail inválido"

    # 2. Verificar se não começa ou termina com "@"
    if email.startswith("@") or email.endswith("@"):
        return "E-mail inválido"

    # 3. Verificar se não contém espaços
    if " " in email:
        return "E-mail inválido"

    # 4. Verificar a estrutura básica do domínio (precisa ter pelo menos um ponto depois do @)
    # Isso é uma checagem simplificada, já que o desafio não pede validação de domínios específicos.
    partes_do_email = email.split('@')
    if len(partes_do_email) != 2: # Deve ter exatamente um '@'
        return "E-mail inválido"

    local_part = partes_do_email[0]
    domain_part = partes_do_email[1]

    if not local_part or not domain_part: # Nenhuma parte pode estar vazia
        return "E-mail inválido"
    if "." not in domain_part: # O domínio precisa ter pelo menos um ponto
        return "E-mail inválido"

    # Se passou por todas as verificações, é válido!
    return "E-mail válido"

# --- Programa Principal ---

# Lê o e-mail a ser validado
email_digitado = input()

# Chama a função de validação e imprime o resultado
resultado = validar_email(email_digitado)
print(resultado)
