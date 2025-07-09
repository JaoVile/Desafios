Sistema Bancário pela terceira vez: agora adaptado para a Programação Orientada a Objetos (POO)

Este projeto refatora o Sistema_Bancario_2 que eu tinha feito antes, aplicando os conceitos fundamentais da Programação Orientada a Objetos (POO) em Python. O objetivo foi criar um código mais limpo, organizado e escalável.

Principais Mudanças Implementadas:
Modelagem de Entidades: As estruturas de dados (dicionários) foram substituídas por classes como Cliente, PessoaFisica, Conta e ContaCorrente.

Encapsulamento de Comportamentos: Funções como sacar e depositar agora são métodos das classes (Conta.sacar()), centralizando as regras de negócio.

Herança e Polimorfismo: A classe ContaCorrente herda de Conta, e as transações Saque e Deposito herdam de uma classe abstrata Transacao.

Histórico de Transações Estruturado: O extrato, antes uma string, foi transformado em uma classe Historico que gerencia uma lista de objetos de transação.

Separação de Responsabilidades: A lógica de interação com o usuário foi separada das regras de negócio, que agora residem dentro das classes.