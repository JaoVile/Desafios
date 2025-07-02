import os
import platform
from collections import defaultdict

def limpar_tela():
    """
    Eu criei esta pequena função para limpar a tela do terminal.
    Achei que a experiência do usuário fica muito melhor assim.
    Eu verifico o sistema operacional porque o comando é 'cls' no Windows e 'clear' no resto.
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def exibir_cabecalho():
    """
    Esta função é só para dar um charme visual.
    Eu a chamo no início para deixar o programa com uma cara mais profissional.
    """
    print("🎉" + "="*45 + "🎉")
    print("      ORGANIZADOR DE EVENTOS INTERATIVO")
    print("🎉" + "="*45 + "🎉\n")

def main():
    """
    Esta é a minha função principal, onde toda a mágica acontece.
    """
    
    # Eu defini os temas disponíveis em uma lista para facilitar a exibição de um menu.
    temas_disponiveis = ["Fotografia", "Viagem", "Tecnologia", "Música", "Esportes"]
    
    # Aqui, eu decidi usar defaultdict(list). É uma ferramenta incrível
    # que cria uma lista vazia para um tema novo na primeira vez que eu o acesso.
    # Isso elimina a necessidade de verificar se a chave já existe no dicionário.
    inscricoes = defaultdict(list)

    # Criei um loop infinito que só para quando o usuário digita 'sair'.
    while True:
        # No início de cada interação, eu limpo a tela e mostro o cabeçalho.
        limpar_tela()
        exibir_cabecalho()

        # Mostro um resumo das inscrições feitas até o momento.
        print("--- INSCRIÇÕES ATUAIS ---")
        if not inscricoes:
            print("Ninguém inscrito ainda.")
        else:
            for tema, participantes in inscricoes.items():
                print(f"  - {tema}: {', '.join(participantes)}")
        print("-" * 28 + "\n")

        # Peço o nome do participante e já uso .strip() para remover espaços extras.
        nome = input("Digite o nome do participante (ou 'sair' para finalizar): ").strip()
        if nome.lower() == 'sair':
            break
        if not nome:
            print("\n❌ Nome não pode ser vazio.")
            input("\nPressione Enter para tentar novamente...")
            continue
            
        # Apresento o menu de temas de forma numerada.
        print("--- ESCOLHA UM TEMA ---")
        for i, tema in enumerate(temas_disponiveis):
            print(f"  {i+1}. {tema}")
        print("-" * 25)
        
        escolha = input(f"Digite o número do tema para '{nome}': ")

        # Eu envolvi a lógica de escolha em um bloco try-except para o programa não quebrar
        # se o usuário digitar um texto em vez de um número.
        try:
            indice_escolhido = int(escolha) - 1
            if 0 <= indice_escolhido < len(temas_disponiveis):
                tema_selecionado = temas_disponiveis[indice_escolhido]
                # Graças ao defaultdict, esta linha é muito simples.
                # Eu simplesmente adiciono o nome à lista do tema correspondente.
                inscricoes[tema_selecionado].append(nome)
                print(f"\n✅ '{nome}' foi inscrito(a) no tema '{tema_selecionado}' com sucesso!")
            else:
                print("\n❌ Opção inválida. Por favor, escolha um número da lista.")
        
        except ValueError:
            print("\n❌ Entrada inválida. Por favor, digite um número.")

        # Faço uma pausa para o usuário ler a mensagem antes da tela limpar.
        input("\nPressione Enter para continuar...")

    # Quando o loop termina, eu apresento o resumo final.
    limpar_tela()
    print("🧑‍🤝‍🧑" * 20)
    print("      LISTA FINAL DE PARTICIPANTES")
    print("🧑‍🤝‍🧑" * 20, "\n")
    
    if not inscricoes:
        print("Nenhuma inscrição foi realizada. Evento cancelado por falta de quorum! 😄")
        return

    # A lógica de exibição final é a mesma do script original.
    for tema, nomes in inscricoes.items():
        nomes_formatados = ", ".join(nomes)
        print(f"{tema}: {nomes_formatados}")
    
    print("\nObrigado por usar o Organizador de Eventos!")

# Eu uso a construção padrão if __name__ == "__main__" para garantir que o meu
# programa só execute a função main() quando eu rodar este arquivo diretamente.
if __name__ == "__main__":
    main()