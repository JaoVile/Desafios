# -*- coding: utf-8 -*-

# Importa a biblioteca necessária
from pathlib import Path

# A função organizar_fila não precisa ser alterada
def organizar_fila(lista_pacientes_str: list[str]) -> list[str]:
    pacientes = []
    for i, paciente_str in enumerate(lista_pacientes_str):
        nome, idade_str, status = paciente_str.split(', ')
        pacientes.append({
            'nome': nome, 
            'idade': int(idade_str), 
            'status': status,
            'chegada': i
        })
    def chave_de_ordenacao(paciente):
        if paciente['status'] == 'urgente': return (0, -paciente['idade'])
        elif paciente['idade'] >= 60: return (1, -paciente['idade'])
        else: return (2, paciente['chegada'])
    pacientes.sort(key=chave_de_ordenacao)
    return [p['nome'] for p in pacientes]


# --- Bloco Principal com Diagnóstico ---
if __name__ == "__main__":
    
    # --- INÍCIO DO CÓDIGO DE DIAGNÓSTICO ---
    print("--- INICIANDO DIAGNÓSTICO ---")
    
    script_path = Path(__file__).resolve()
    script_dir = script_path.parent
    arquivo_de_entradas = script_dir / 'entradas.txt'

    print(f"1. O script está localizado em (caminho completo): {script_path}")
    print(f"2. A pasta onde o script está é: {script_dir}")
    print(f"3. O script está procurando pelo arquivo em: {arquivo_de_entradas}")
    # A linha abaixo é a mais importante. Ela pergunta ao sistema operacional se o arquivo existe.
    print(f"4. O arquivo realmente existe nesse caminho? -> {arquivo_de_entradas.exists()}")

    print("--- FIM DO DIAGNÓSTICO ---\n")
    # --- FIM DO CÓDIGO DE DIAGNÓSTICO ---

    # O script só continua se o diagnóstico for positivo
    if not arquivo_de_entradas.exists():
        print(f"ERRO CRÍTICO: Diagnóstico falhou.")
        print("O Passo 4 acima mostrou 'False'. Isso significa que o arquivo 'entradas.txt' NÃO está na mesma pasta do script ou o nome está incorreto (verifique se não é 'entradas.txt.txt').")
        exit()

    # Se o diagnóstico passou, o resto do código executa normalmente.
    print("Diagnóstico OK. Executando testes a partir de 'entradas.txt'...\n")
    
    with open(arquivo_de_entradas, 'r', encoding='utf-8') as f:
        casos_de_teste = f.read().strip().split('---')

    for i, caso in enumerate(casos_de_teste):
        linhas = [linha for linha in caso.strip().split('\n') if linha and not linha.startswith('#')]
        
        if not linhas: continue
        
        dados_pacientes = linhas[1:]
        ordem_atendimento = organizar_fila(dados_pacientes)
        resultado_formatado = f"Ordem de Atendimento: {', '.join(ordem_atendimento)}"
        print(f"Resultado Teste {i + 1}: {resultado_formatado}")
