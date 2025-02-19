# 💳 Sistema Simples de Processamento de Pagamentos (POO + SOLID)

Este é um **Sistema Simples de Processamento de Pagamentos** implementado em Python utilizando **Programação Orientada a Objetos (POO)** e os **Princípios SOLID** para fins de estudo.  

## 🚀 Funcionalidades

- Processa pagamentos via:
  - **Pix** (Sistema de pagamento instantâneo brasileiro)
  - **Cartão de Crédito**
  - **Boleto (Invoice)**
- Fácil extensão para novos métodos de pagamento.
- Processamento centralizado com uma classe responsável pela orquestração dos pagamentos.

## 🏗️ Conceitos de POO Aplicados

✔ **Encapsulamento** – Uso de atributos protegidos e métodos públicos.  
✔ **Herança e Polimorfismo** – Classe base `Payment` com várias subclasses para diferentes métodos de pagamento.  
✔ **Abstração** – Classe abstrata `Payment` define uma interface comum para todos os tipos de pagamento.  

## 🧑‍🏫 Princípios SOLID Aplicados

✔ **SRP (Princípio da Responsabilidade Única)** – Cada classe tem uma única responsabilidade.  
✔ **OCP (Princípio Aberto/Fechado)** – Novos métodos de pagamento podem ser adicionados sem modificar o código existente.  
✔ **LSP (Princípio da Substituição de Liskov)** – Subclasses podem ser usadas de forma intercambiável com a classe base `Payment`.  
✔ **ISP (Princípio da Segregação de Interface)** – `Payment` define apenas a interface necessária para suas subclasses.  
✔ **DIP (Princípio da Inversão de Dependência)** – `PaymentProcessor` depende da abstração `Payment`, não de implementações concretas.  

## 🛠️ Como Executar o Projeto

1. Clone o repositório:
   ```sh
   git clone https://
   cd poo-solid-payment-system
   ```
2. Execute o script:
   ```sh
   python main.py
   ```

## 📂 Estrutura do Projeto

```
📂 poo-solid-payment-system
│── 📄 main.py        # Código principal do sistema
│── 📄 README.md      # Documentação do projeto
```
