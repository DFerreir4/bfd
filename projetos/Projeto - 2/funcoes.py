import os
from datetime import datetime
from cadastro_eventos import CadastroEventos

# Função para limpar a tela (Windows e Linux/Mac)
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Função de pausa para exibir mensagens antes de voltar ao menu
def pausar(msg="\nPressione ENTER para voltar..."):
    input(msg)
    limpar_tela()

# Função auxiliar para validar entradas de texto
def validar_texto(campo):
    while True:
        valor = input(f"{campo}: ").strip()
        if valor:
            return valor
        else:
            input(f"ERRO! : O campo '{campo}' não pode ficar em branco. Pressione ENTER para tentar novamente.")

# Função auxiliar para validar número inteiro positivo
def validar_inteiro(campo):
    while True:
        valor = input(f"{campo}: ").strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        else:
            input(f"ERRO! : O campo '{campo}' deve ser um número inteiro positivo. Pressione ENTER para tentar novamente.")

# Função auxiliar para validar número decimal
def validar_float(campo):
    while True:
        valor = input(f"{campo}: ").strip()
        try:
            numero = float(valor)
            if numero >= 0:
                return numero
            else:
                input(f"ERRO! : O campo '{campo}' deve ser um número maior ou igual a zero. Pressione ENTER para tentar novamente.")
        except ValueError:
            input(f"ERRO! : O campo '{campo}' deve ser numérico. Pressione ENTER para tentar novamente.")

# Função auxiliar para validar data no formato correto
def validar_data(campo):
    while True:
        valor = input(f"{campo} (DD/MM/AAAA): ").strip()
        try:
            data = datetime.strptime(valor, "%d/%m/%Y")
            if data.date() < datetime.today().date():
                input(f"ERRO! : A data não pode ser anterior à data atual. Pressione ENTER para tentar novamente.")
            else:
                return data.strftime("%d/%m/%Y")
        except ValueError:
            input(f"ERRO! : O campo '{campo}' deve estar no formato DD/MM/AAAA. Pressione ENTER para tentar novamente.")

# Função de relatórios
def relatorios():
    while True:
        print("##### RELATÓRIOS #####")
        print("1 - Número total de inscritos por evento")
        print("2 - Lista de eventos com vagas disponíveis")
        print("3 - Receita total por evento")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n#### INSCRITOS POR EVENTO ####")
            if not CadastroEventos._eventos:
                print("Nenhum evento cadastrado.")
            else:
                for evento in CadastroEventos._eventos:
                    print(f"{evento.nome}: {len(evento.inscritos)} inscritos")
            pausar()

        elif opcao == "2":
            print("\n#### EVENTOS COM VAGAS DISPONÍVEIS ####")
            if not CadastroEventos._eventos:
                print("Nenhum evento cadastrado.")
            else:
                for evento in CadastroEventos._eventos:
                    vagas_restantes = evento.capacidade_maxima - len(evento.inscritos)
                    if vagas_restantes > 0:
                        print(f"{evento.nome} -> {len(evento.inscritos)}/{evento.capacidade_maxima} inscritos")
            pausar()

        elif opcao == "3":
            print("\n##### RECEITA TOTAL POR EVENTO #####")
            if not CadastroEventos._eventos:
                print("Nenhum evento cadastrado.")
            else:
                for evento in CadastroEventos._eventos:
                    receita = len(evento.inscritos) * evento.preco_ingresso
                    print(f"{evento.nome}: R${receita:.2f}")
            pausar()

        elif opcao == "0":
            limpar_tela()
            break
        else:
            input("Opção INVÁLIDA, pressione ENTER para tentar novamente.")
            limpar_tela()
