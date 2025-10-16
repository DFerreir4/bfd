# Sistema de Gerenciamento de Eventos

Este projeto é um **sistema de gerenciamento de eventos** desenvolvido em **Python**, que permite cadastrar eventos, inscrever participantes, realizar check-ins, cancelar inscrições e gerar relatórios.  
Ele foi criado com foco em **organização, validação de dados e persistência das informações em arquivo `.json`**, garantindo que os dados sejam mantidos mesmo após o fechamento do programa.

---

## Funcionalidades Principais

 **Cadastrar Evento**  
- Permite criar novos eventos informando nome, data, local, capacidade, categoria e preço.  
- Impede o cadastro de eventos duplicados.  
- Valida todos os campos antes de salvar.  

 **Listar Eventos e Buscar por Categoria/Data**  
- Exibe todos os eventos cadastrados com detalhes.  
- Permite filtrar por **categoria** ou **data (DD/MM/AAAA)**.

 **Inscrever Participante**  
- Inscreve participantes em eventos disponíveis.  
- Impede inscrições em eventos lotados.

 **Realizar Check-in**  
- Marca presença de participantes nos eventos.  
- Registra informações para exibição em relatórios.

 **Cancelar Inscrição**  
- Cancela a inscrição de um participante em um evento.  

 **Relatórios**  
- Exibe lista de participantes com check-in realizado.  
- Permite busca de participantes que fizeram check-in por data.

 **Persistência de Dados (.json)**  
- Todos os cadastros (eventos e inscrições) são salvos automaticamente em arquivos JSON.  
- Ao abrir o sistema novamente, os dados são carregados.

---

## Estrutura do Projeto

    sistema_eventos/
    │
    ├── main.py # Arquivo principal que executa o sistema e exibe o menu
    ├── cadastro_eventos.py # Classe responsável por gerenciar eventos
    ├── inscricoes_participantes.py # Classe responsável pelas inscrições e check-ins
    ├── funcoes.py # Funções auxiliares (validação, limpar tela, etc.)
    ├── eventos.json # Arquivo JSON onde os dados são salvos automaticamente
    └── README.md # Este arquivo de documentação



##  Requisitos e Instalação

###  Requisitos Mínimos
- **Python 3.8 ou superior**
- **Sistema operacional:** Windows, macOS ou Linux

###  Instalação

1. **Clone este repositório** (ou copie os arquivos para uma pasta local):
   git clone https://github.com/DFerreir4/bfd.git
   cd sistema-eventos


## Como Executar o Sistema

Execute o arquivo principal main.py no terminal:

python main.py


O menu principal será exibido com as opções disponíveis:

            ##############################
            ###### MENU PRINCIPAL #######
            ##############################
            | 1 - Cadastrar evento       |
            | 2 - Listar eventos         |
            | 3 - Inscrever participante |
            | 4 - Realizar check-in      |
            | 5 - Cancelar inscrição     |
            | 6 - Relatórios             |
            | 0 - Sair                   |
            ------------------------------
            Escolha uma opção:

## Sobre a Persistência de Dados

Os dados do sistema são automaticamente salvos em um arquivo chamado eventos.json localizado na mesma pasta do projeto.
Esse arquivo é lido toda vez que o programa inicia e atualizado quando há novos cadastros, inscrições ou check-ins.

🧠 Conceitos Utilizados

Programação Orientada a Objetos (POO):

Uso de classes e instâncias para representar eventos e inscrições.

Encapsulamento e validação de dados

Tratamento de erros e exceções

Persistência em JSON

Estrutura modularizada (arquivos separados por responsabilidade)

## Autor

    Diego Andrade
    Desenvolvido como parte de um projeto de aprendizado em Python e Programação Orientada a Objetos.
    

## Licença

    Este projeto é de uso livre para fins de estudo e aprendizado.
    Sinta-se à vontade para modificar, melhorar e compartilhar!


