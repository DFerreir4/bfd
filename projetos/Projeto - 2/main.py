import os
from cadastro_eventos import CadastroEventos
from inscricoes_participantes import InscricoesParticipantes

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar(msg="\nPressione ENTER para voltar..."):
    input(msg)
    limpar_tela()

def relatorios():
    while True:
        print("===== RELATÓRIOS =====")
        print("1 - Número total de inscritos por evento")
        print("2 - Lista de eventos com vagas disponíveis")
        print("3 - Receita total por evento")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n=== INSCRITOS POR EVENTO ===")
            if not CadastroEventos._eventos:
                print("Nenhum evento cadastrado.")
            else:
                for evento in CadastroEventos._eventos:
                    print(f"{evento.nome}: {len(evento.inscritos)} inscritos")
            pausar()

        elif opcao == "2":
            print("\n=== EVENTOS COM VAGAS DISPONÍVEIS ===")
            if not CadastroEventos._eventos:
                print("Nenhum evento cadastrado.")
            else:
                for evento in CadastroEventos._eventos:
                    vagas_restantes = evento.capacidade_maxima - len(evento.inscritos)
                    if vagas_restantes > 0:
                        print(f"{evento.nome} -> {len(evento.inscritos)}/{evento.capacidade_maxima} inscritos")
            pausar()

        elif opcao == "3":
            print("\n=== RECEITA TOTAL POR EVENTO ===")
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
            print("Opção inválida, tente novamente.")
            pausar()

def menu():
    while True:
        print("===== MENU PRINCIPAL =====")
        print("1 - Cadastrar evento")
        print("2 - Listar eventos")
        print("3 - Buscar evento por categoria/data")
        print("4 - Inscrever participante")
        print("5 - Cancelar inscrição")
        print("6 - Realizar check-in")
        print("7 - Relatórios")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                nome = input("Nome do evento: ")
                data = input("Data do evento (DD/MM/AAAA): ")
                local = input("Local do evento: ")
                capacidade = int(input("Capacidade máxima: "))
                categoria = input("Categoria: ")
                preco = float(input("Preço do ingresso: "))
                evento = CadastroEventos(nome, data, local, capacidade, categoria, preco)
                print(f"\nEvento '{evento.nome}' cadastrado com sucesso!")
            except Exception as e:
                print("Erro:", e)
            pausar()

        elif opcao == "2":
            print("\n=== LISTA DE EVENTOS ===")
            print(CadastroEventos.listar_eventos())
            pausar()

        elif opcao == "3":
            tipo = input("Buscar por (categoria/data): ").strip().lower()
            if tipo == "categoria":
                cat = input("Digite a categoria: ")
                resultados = CadastroEventos.buscar_eventos(categoria=cat)
            elif tipo == "data":
                data = input("Digite a data (DD/MM/AAAA): ")
                resultados = CadastroEventos.buscar_eventos(data=data)
            else:
                print("Opção inválida!")
                pausar()
                continue

            print("\n=== RESULTADOS ===")
            if isinstance(resultados, str):
                print(resultados)
            else:
                for evento in resultados:
                    print(evento, "\n")
            pausar()

        elif opcao == "4":
            try:
                if not CadastroEventos._eventos:
                    print("Nenhum evento cadastrado.")
                    pausar()
                    continue
                print("\n=== EVENTOS DISPONÍVEIS ===")
                for i, evento in enumerate(CadastroEventos._eventos, start=1):
                    print(f"{i} - {evento.nome} ({len(evento.inscritos)}/{evento.capacidade_maxima} vagas)")
                escolha = int(input("Escolha o número do evento: ")) - 1
                evento = CadastroEventos._eventos[escolha]

                nome = input("Nome do participante: ")
                email = input("E-mail do participante: ")
                participante = InscricoesParticipantes(nome, email, evento)
                print(f"\nInscrição de {participante.nome} realizada com sucesso!")
            except Exception as e:
                print("Erro:", e)
            pausar()

        elif opcao == "5":
            try:
                email = input("Digite o e-mail do participante: ")
                encontrado = False
                for evento in CadastroEventos._eventos:
                    for inscrito in evento.inscritos:
                        if inscrito.email == email:
                            print(inscrito.cancelar_inscricao())
                            encontrado = True
                            break
                if not encontrado:
                    print("Participante não encontrado.")
            except Exception as e:
                print("Erro:", e)
            pausar()

        elif opcao == "6":
            try:
                email = input("Digite o e-mail do participante: ")
                encontrado = False
                for evento in CadastroEventos._eventos:
                    for inscrito in evento.inscritos:
                        if inscrito.email == email:
                            print(inscrito.realizar_checkin())
                            encontrado = True
                            break
                if not encontrado:
                    print("Participante não encontrado.")
            except Exception as e:
                print("Erro:", e)
            pausar()

        elif opcao == "7":
            limpar_tela()
            relatorios()

        elif opcao == "0":
            print("Saindo... Até logo! 👋")
            break

        else:
            print("Opção inválida, tente novamente.")
            pausar()

if __name__ == "__main__":
    limpar_tela()
    menu()
