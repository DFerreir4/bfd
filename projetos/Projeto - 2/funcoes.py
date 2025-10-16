# Importa módulos e classes necessários para o funcionamento das funções
import os  # usado para limpar a tela do terminal
from datetime import datetime  # usado para trabalhar com datas
from cadastro_eventos import CadastroEventos  # permite acessar os eventos e gerar relatórios

# ------------------------------------------------------------
# FUNÇÃO: limpar_tela()
# ------------------------------------------------------------
# Essa função apaga o conteúdo do terminal e deixa a tela limpa.
# Isso ajuda a deixar o programa mais organizado e fácil de ler.
def limpar_tela():
    # Se o sistema for Windows, usa o comando "cls"
    # Se for Linux ou Mac, usa o comando "clear"
    os.system("cls" if os.name == "nt" else "clear")


# ------------------------------------------------------------
# FUNÇÃO: pausar()
# ------------------------------------------------------------
# Essa função serve para "pausar" o programa e mostrar uma mensagem.
# Ela espera o usuário pressionar ENTER antes de continuar.
def pausar(msg="\nPressione ENTER para voltar..."):
    # Exibe a mensagem passada como parâmetro e espera o ENTER
    input(msg)
    # Depois de pressionar ENTER, a tela é limpa
    limpar_tela()


# ------------------------------------------------------------
# FUNÇÃO: validar_texto()
# ------------------------------------------------------------
# Essa função garante que o usuário digite algo no campo de texto.
# Se o campo estiver vazio, ele mostra um erro e pede novamente.
def validar_texto(campo):
    while True:
        valor = input(f"{campo}: ").strip()  # Pede o valor e remove espaços extras
        if valor:  # Se o usuário digitou algo
            return valor  # Retorna o valor digitado
        else:
            # Se o campo estiver vazio, mostra erro e pede ENTER para tentar de novo
            input(f"ERRO! : O campo '{campo}' não pode ficar em branco. Pressione ENTER para tentar novamente.")


# ------------------------------------------------------------
# FUNÇÃO: validar_inteiro()
# ------------------------------------------------------------
# Essa função garante que o valor digitado seja um número inteiro positivo.
# Ela é usada, por exemplo, para a capacidade máxima de um evento.
def validar_inteiro(campo):
    while True:
        valor = input(f"{campo}: ").strip()
        # .isdigit() verifica se o valor tem apenas números
        if valor.isdigit() and int(valor) > 0:
            return int(valor)  # Converte para inteiro e retorna
        else:
            input(f"ERRO! : O campo '{campo}' deve ser um número inteiro positivo. Pressione ENTER para tentar novamente.")


# ------------------------------------------------------------
# FUNÇÃO: validar_float()
# ------------------------------------------------------------
# Essa função garante que o valor digitado seja um número decimal (float).
# Usada, por exemplo, para o preço do ingresso.
def validar_float(campo):
    while True:
        valor = input(f"{campo}: ").strip()
        try:
            # Tenta converter o valor digitado para float
            numero = float(valor)
            if numero >= 0:
                return numero
            else:
                input(f"ERRO! : O campo '{campo}' deve ser um número maior ou igual a zero. Pressione ENTER para tentar novamente.")
        except ValueError:
            # Se o valor não for um número válido, mostra mensagem de erro
            input(f"ERRO! : O campo '{campo}' deve ser numérico. Pressione ENTER para tentar novamente.")


# ------------------------------------------------------------
# FUNÇÃO: validar_data()
# ------------------------------------------------------------
# Essa função garante que a data digitada esteja no formato certo (DD/MM/AAAA)
# e que a data não seja anterior ao dia de hoje.
def validar_data(campo):
    while True:
        valor = input(f"{campo} (DD/MM/AAAA): ").strip()
        try:
            # Tenta converter o texto digitado para uma data real
            data = datetime.strptime(valor, "%d/%m/%Y")
            # Se a data for no passado, mostra erro
            if data.date() < datetime.today().date():
                input(f"ERRO! : A data não pode ser anterior à data atual. Pressione ENTER para tentar novamente.")
            else:
                # Retorna a data formatada corretamente
                return data.strftime("%d/%m/%Y")
        except ValueError:
            # Caso o formato esteja errado, mostra uma mensagem explicando o erro
            input(f"ERRO! : O campo '{campo}' deve estar no formato DD/MM/AAAA. Pressione ENTER para tentar novamente.")


# ------------------------------------------------------------
# FUNÇÃO: relatorios()
# ------------------------------------------------------------
# Essa função mostra várias opções de relatórios sobre os eventos e participantes.
def relatorios():
    while True:
        # Exibe o menu de relatórios
        print("##### RELATÓRIOS #####")
        print("1 - Número total de inscritos por evento")
        print("2 - Lista de eventos com vagas disponíveis")
        print("3 - Lista de participantes com check-in realizado")
        print("4 - Receita total por evento")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        # ------------------------------------------------------------
        # OPÇÃO 1 -> Mostra o número total de inscritos em cada evento
        # ------------------------------------------------------------
        if opcao == "1":
            print("\n#### INSCRITOS POR EVENTO ####")
            if not CadastroEventos._eventos:  # Se não houver eventos cadastrados
                print("Nenhum evento cadastrado.")
            else:
                # Percorre cada evento e mostra quantos inscritos tem
                for evento in CadastroEventos._eventos:
                    print(f"{evento.nome}: {len(evento.inscritos)} inscritos")
            pausar()

        # ------------------------------------------------------------
        # OPÇÃO 2 -> Lista os eventos que ainda têm vagas disponíveis
        # ------------------------------------------------------------
        elif opcao == "2":
            print("\n#### EVENTOS COM VAGAS DISPONÍVEIS ####")
            if not CadastroEventos._eventos:
                print("Nenhum evento cadastrado.")
            else:
                for evento in CadastroEventos._eventos:
                    # Calcula quantas vagas ainda restam
                    vagas_restantes = evento.capacidade_maxima - len(evento.inscritos)
                    if vagas_restantes > 0:
                        print(f"{evento.nome} -> {len(evento.inscritos)}/{evento.capacidade_maxima} inscritos")
            pausar()

        # ------------------------------------------------------------
        # OPÇÃO 3 -> Lista de participantes que já fizeram check-in
        # ------------------------------------------------------------
        elif opcao == "3":
            print("\n##### LISTA DE PARTICIPANTES COM CHECK-IN REALIZADO #####")
            checkins_encontrados = False  # variável de controle para saber se encontrou alguém

            # Percorre todos os eventos e todos os participantes
            for evento in CadastroEventos._eventos:
                for participante in evento.inscritos:
                    # Verifica se o participante tem o atributo checkin e se ele é True
                    if hasattr(participante, "checkin") and participante.checkin:
                        checkins_encontrados = True
                        print(f"Evento: {evento.nome}")
                        print(f"Data do Evento: {evento.data.strftime('%d/%m/%Y')}")
                        print(f"Categoria: {evento.categoria}")
                        print(f"Participante: {participante.nome}")
                        print(f"E-mail: {participante.email}\n")

            # Caso nenhum check-in tenha sido encontrado
            if not checkins_encontrados:
                print("Nenhum participante realizou check-in ainda.")

            # ------------------------------------------------------------
            # PERGUNTA -> Deseja buscar participantes por data específica?
            # ------------------------------------------------------------
            escolha = input("\nVocê deseja fazer uma busca de participantes por data? (s/n): ").strip().lower()
            if escolha == "s":
                # Pede ao usuário a data desejada
                data_busca = input("Digite a data (DD/MM/AAAA): ").strip()

                try:
                    # Converte a data digitada para um formato de data real
                    data_obj = datetime.strptime(data_busca, "%d/%m/%Y")
                    encontrou = False  # variável de controle
                    print("\n##### RESULTADOS DA BUSCA #####")

                    # Percorre os eventos
                    for evento in CadastroEventos._eventos:
                        # Se a data do evento for igual à buscada
                        if evento.data.date() == data_obj.date():
                            # Percorre os inscritos do evento
                            for participante in evento.inscritos:
                                # Mostra apenas quem fez check-in
                                if hasattr(participante, "checkin") and participante.checkin:
                                    encontrou = True
                                    print(f"Evento: {evento.nome}")
                                    print(f"Data do Evento: {evento.data.strftime('%d/%m/%Y')}")
                                    print(f"Categoria: {evento.categoria}")
                                    print(f"Participante: {participante.nome}")
                                    print(f"E-mail: {participante.email}\n")

                    # Caso não encontre nenhum resultado
                    if not encontrou:
                        print("Nenhum check-in encontrado para a data informada.")

                except ValueError:
                    # Caso a data esteja no formato errado
                    print("Formato de data inválido. Use DD/MM/AAAA.")
                pausar()
            else:
                limpar_tela()

        # ------------------------------------------------------------
        # OPÇÃO 4 -> Mostra a receita total por evento (quantos pagaram × preço do ingresso)
        # ------------------------------------------------------------
        elif opcao == "4":
            print("\n##### RECEITA TOTAL POR EVENTO #####")
            if not CadastroEventos._eventos:
                print("Nenhum evento cadastrado.")
            else:
                # Calcula e exibe a receita de cada evento
                for evento in CadastroEventos._eventos:
                    receita = len(evento.inscritos) * evento.preco_ingresso
                    print(f"{evento.nome}: R${receita:.2f}")
            pausar()

        # ------------------------------------------------------------
        # OPÇÃO 0 -> Sai do menu de relatórios e volta ao menu principal
        # ------------------------------------------------------------
        elif opcao == "0":
            limpar_tela()
            break

        # ------------------------------------------------------------
        # Caso o usuário digite uma opção inválida
        # ------------------------------------------------------------
        else:
            input("Opção INVÁLIDA, pressione ENTER para tentar novamente.")
            limpar_tela()
