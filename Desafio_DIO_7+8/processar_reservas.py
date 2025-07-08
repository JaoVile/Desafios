# Arquivo: processar_reservas.py

def processar_reservas():
    # Esta linha vai PARAR e esperar você digitar os quartos disponíveis
    print("Digite os quartos disponíveis e aperte Enter:")
    quartos_disponiveis = set(map(int, input().split()))
    
    # Esta linha vai PARAR de novo e esperar as reservas
    print("Digite as reservas solicitadas e aperte Enter:")
    reservas_solicitadas = list(map(int, input().split()))

    confirmadas = []
    recusadas = []

    for reserva in reservas_solicitadas:
        if reserva in quartos_disponiveis:
            confirmadas.append(reserva)
        else:
            recusadas.append(reserva)

    # Saída dos resultados
    print("\n--- Resultado ---") # Adicionei um separador para ficar claro
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()