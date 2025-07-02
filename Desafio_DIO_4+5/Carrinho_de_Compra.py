import os
import platform

def limpar_tela():
    """Limpa a tela do terminal para uma melhor experiência do usuário."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def exibir_cabecalho():
    """Mostra o cabeçalho do programa com a promoção."""
    print("🍎" + "="*40 + "🍊")
    print("      BEM-VINDO AO HORTIFRUTI DO JAO!")
    print("🍊" + "="*40 + "🍎")
    print("\nNossa super promoção de hoje:")
    print("  - COMPRE 3, LEVE +1 DE GRAÇA! (Leve 4 unidades e pague apenas 3!)\n")

def main():
    """Função principal que gerencia a experiência de compra interativa."""
    
    estoque = {
        "Maçã": 2.50,
        "Banana": 1.80,
        "Laranja": 2.20,
        "Pera": 3.10,
        "Uva (cacho)": 8.50,
        "Manga": 4.90
    }
    lista_produtos = list(estoque.keys())
    
    carrinho = {}

    while True:
        limpar_tela()
        exibir_cabecalho()

        print("--- SEU CARRINHO ATUAL ---")
        if not carrinho:
            print("Carrinho vazio.")
        else:
            for produto, qtd in carrinho.items():
                print(f"  - {produto}: {qtd} unidade(s)")
        print("-" * 28 + "\n")

        print("--- NOSSOS PRODUTOS ---")
        for i, produto in enumerate(lista_produtos):
            preco = estoque[produto]
            print(f"  {i+1}. {produto:12} - R$ {preco:.2f}")
        print("-" * 25)
        
        escolha = input("Digite o número do produto para adicionar ou 'sair' para finalizar: ").lower()

        if escolha == 'sair':
            break
        
        try:
            indice_escolhido = int(escolha) - 1
            if 0 <= indice_escolhido < len(lista_produtos):
                produto_selecionado = lista_produtos[indice_escolhido]
                carrinho[produto_selecionado] = carrinho.get(produto_selecionado, 0) + 1
                print(f"\n✅ '{produto_selecionado}' adicionado ao carrinho!")

                # --- LÓGICA DE NOTIFICAÇÃO DA OFERTA ---
                quantidade_atual = carrinho[produto_selecionado]
                # Se a quantidade for um múltiplo de 3, o cliente ativou a oferta!
                if quantidade_atual % 3 == 0:
                    print("\n" + "✨" * 15)
                    print(f"  OFERTA ATIVADA para {produto_selecionado}!")
                    print(f"  Você já tem {quantidade_atual}. Adicione a próxima DE GRAÇA!")
                    print("✨" * 15)

            else:
                print("\n❌ Opção inválida. Por favor, escolha um número da lista.")
        
        except ValueError:
            print("\n❌ Entrada inválida. Digite um número ou 'sair'.")

        input("\nPressione Enter para continuar...")

    # --- FINALIZAÇÃO DA COMPRA ---
    limpar_tela()
    print("🛒" * 20)
    print("        RECIBO DA SUA COMPRA")
    print("🛒" * 20, "\n")
    
    total_original = 0
    total_descontos = 0

    if not carrinho:
        print("Você não comprou nada. Volte sempre!")
        return

    for produto, quantidade in carrinho.items():
        preco_unitario = estoque[produto]
        subtotal_produto = quantidade * preco_unitario
        total_original += subtotal_produto
        
        print(f"Produto: {produto} ({quantidade}x R${preco_unitario:.2f})")
        print(f"  Subtotal original: R$ {subtotal_produto:.2f}")

        # A lógica no final permanece a mesma: a cada 4 itens, 1 é grátis.
        unidades_gratis = quantidade // 4
        
        if unidades_gratis > 0:
            desconto = unidades_gratis * preco_unitario
            total_descontos += desconto
            print(f"  -> Promo 'Compre 3, Leve +1': -R$ {desconto:.2f} ({unidades_gratis} unidade(s) grátis)")
        
        print("-" * 30)

    total_final = total_original - total_descontos
    
    print("\n" + "="*30)
    print(f"TOTAL ORIGINAL:   R$ {total_original:.2f}")
    print(f"TOTAL DESCONTOS: -R$ {total_descontos:.2f}")
    print("="*30)
    print(f"VALOR A PAGAR:    R$ {total_final:.2f}")
    print("\nObrigado pela sua compra! Volte sempre!")

if __name__ == "__main__":
    main()