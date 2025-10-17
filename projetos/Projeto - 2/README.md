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

## Diagrama de Classes UML
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/6e87f434-3863-4b8c-8840-98a8deaf8f24" />

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

## Cenários de Interação do Usuário

Esses cenários descrevem possíveis interações que um usuário pode ter com o sistema de gerenciamento de eventos.

- 1. Cadastrar um novo evento

Como um organizador, eu quero cadastrar um novo evento informando nome, data, local, categoria, capacidade e preço do ingresso,
para que os participantes possam se inscrever e eu possa controlar as vagas disponíveis.

- 2. Listar e buscar eventos

Como um usuário, eu quero visualizar todos os eventos cadastrados e também buscar eventos por categoria ou data,
para que eu possa encontrar facilmente eventos do meu interesse.

- 3. Inscrever participante

Como um participante, eu quero me inscrever em um evento informando meu nome e e-mail,
para que eu possa garantir minha vaga antes que as inscrições se encerrem.

- 4. Evitar inscrições duplicadas

Como um participante, eu quero ser avisado se já estiver inscrito em um evento,
para que eu não faça inscrições duplicadas usando o mesmo e-mail.

- 5. Realizar check-in no evento

Como um participante, eu quero registrar meu check-in no evento,
para que os organizadores saibam que compareci.

- 6. Cancelar uma inscrição

Como um participante, eu quero cancelar minha inscrição em um evento,
para que outra pessoa possa ocupar minha vaga.

- 7. Gerar relatórios de eventos

Como um organizador, eu quero visualizar relatórios com o número total de inscritos,
eventos com vagas disponíveis e a lista de participantes que realizaram check-in,
para que eu possa acompanhar o desempenho dos eventos e controlar a receita.

- 8. Salvar e carregar dados automaticamente

Como um usuário, eu quero que o sistema salve automaticamente todos os cadastros em um arquivo .json,
para que as informações não se percam ao fechar o programa.


##  Requisitos e Instalação

###  Requisitos Mínimos
- **Python 3.8 ou superior**
- **Sistema operacional:** Windows, macOS ou Linux

###  Instalação

1. **Clone este repositório** (ou copie os arquivos para uma pasta local):
    
        git clone https://github.com/DFerreir4/bfd/tree/main/projetos/Projeto%20-%202

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

## Conceitos Utilizados

Programação Orientada a Objetos (POO):

Uso de classes e instâncias para representar eventos e inscrições.

Encapsulamento e validação de dados

Tratamento de erros e exceções

Persistência em JSON

Estrutura modularizada (arquivos separados por responsabilidade)

## Autor

Diego Ferreira
Desenvolvido como parte de um projeto de aprendizado em Python e Programação Orientada a Objetos.
    

## Licença

Este projeto é de uso livre para fins de estudo e aprendizado.
Sinta-se à vontade para modificar, melhorar e compartilhar!


