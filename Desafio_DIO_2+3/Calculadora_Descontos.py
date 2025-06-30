# --- Desafio: Calculadora de Descontos Interativa ---

# Dicionário de descontos: chave é o cupom, valor é o fator de multiplicação.
# Formato: "CUPOM": FATOR_DESCONTO (ex: 1.0 para 0%, 0.90 para 10%)
descontos = {
    "DESCONTO10": 0.90,
    "DESCONTO20": 0.80,
    "SEM_DESCONTO": 1.00,
}

# --- Função para obter um preço válido ---
def obter_preco():
    while True:
        try:
            # Solicita o preço ao usuário
            preco_str = input("Informe o preço original do produto: ")
            preco = float(preco_str)
            if preco >= 0:
                return preco # Retorna o preço se for válido
            else:
                print("Erro: O preço não pode ser negativo. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número para o preço.")

# --- Função Principal do Programa ---
def main():
    print("--- Bem-vindo(a) à nossa Calculadora de Descontos! ---")

    # Obtém o preço original validado
    preco_original = obter_preco()

    # Solicita o código do cupom ao usuário
    codigo_cupom = input("Digite o código do cupom de desconto: ")

    # Processa o cupom (convertendo para maiúsculas para não diferenciar case)
    cupom_processado = codigo_cupom.strip().upper() # .strip() remove espaços extras antes/depois

    # Busca o fator de desconto. Se o cupom não existir, usa 1.0 (sem desconto).
    fator_desconto = descontos.get(cupom_processado, 1.0)

    # Aplica o desconto
    preco_final = preco_original * fator_desconto

    # --- Saída do Resultado ---
    print("\n--- Resultado do Cálculo ---")
    if fator_desconto == 1.0 and cupom_processado != "SEM_DESCONTO":
        # Mensagem específica se o cupom não foi encontrado ou é inválido
        print(f"O cupom '{codigo_cupom}' não foi reconhecido ou é inválido.")
        print(f"Preço final: R$ {preco_original:.2f}")
    else:
        # Mensagem padrão para descontos aplicados ou cupom SEM_DESCONTO
        if cupom_processado == "SEM_DESCONTO":
            print("Nenhum desconto aplicado.")
        elif fator_desconto != 1.0:
            desconto_percentual = (1 - fator_desconto) * 100
            print(f"Cupom '{codigo_cupom}' aplicado ({desconto_percentual:.0f}% de desconto).")
        
        print(f"Preço final: R$ {preco_final:.2f}")

# Chama a função principal para iniciar o programa
if __name__ == "__main__":
    main()
