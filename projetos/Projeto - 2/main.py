from cadastro_eventos import CadastroEventos
from inscricoes_participantes import InscricoesParticipantes

def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
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
                print(f"Evento '{evento.nome}' cadastrado com sucesso!")
            except Exception as e:
                print("Erro:", e)

        elif opcao == "2":
            print("\n=== LISTA DE EVENTOS ===")
            print(CadastroEventos.listar_eventos())

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
                continue

            print("\n=== RESULTADOS ===")
            if isinstance(resultados, str):
                print(resultados)
            else:
                for evento in resultados:
                    print(evento, "\n")

        elif opcao == "4":
            try:
                if not CadastroEventos._eventos:
                    print("Nenhum evento cadastrado.")
                    continue
                print("\n=== EVENTOS DISPONÍVEIS ===")
                for i, evento in enumerate(CadastroEventos._eventos, start=1):
                    print(f"{i} - {evento.nome} ({len(evento.inscritos)}/{evento.capacidade_maxima} vagas)")
                escolha = int(input("Escolha o número do evento: ")) - 1
                evento = CadastroEventos._eventos[escolha]

                nome = input("Nome do participante: ")
                email = input("E-mail do participante: ")
                participante = InscricoesParticipantes(nome, email, evento)
                print(f"Inscrição de {participante.nome} realizada com sucesso!")
            except Exception as e:
                print("Erro:", e)

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

        elif opcao == "7":
            print("\n===== RELATÓRIOS =====")
            print("1 - Número total de inscritos por evento")
            print("2 - Lista de eventos com vagas disponíveis")
            print("3 - Receita total por evento")
            rel_opcao = input("Escolha uma opção: ")

            if rel_opcao == "1":
                print("\n=== INSCRITOS POR EVENTO ===")
                for evento in CadastroEventos._eventos:
                    print(f"{evento.nome}: {len(evento.inscritos)} inscritos")

            elif rel_opcao == "2":
                print("\n=== EVENTOS COM VAGAS DISPONÍVEIS ===")
                for evento in CadastroEventos._eventos:
                    vagas_restantes = evento.capacidade_maxima - len(evento.inscritos)
                    if vagas_restantes > 0:
                        print(f"{evento.nome} -> {len(evento.inscritos)}/{evento.capacidade_maxima} inscritos")

            elif rel_opcao == "3":
                print("\n=== RECEITA TOTAL POR EVENTO ===")
                for evento in CadastroEventos._eventos:
                    receita = len(evento.inscritos) * evento.preco_ingresso
                    print(f"{evento.nome}: R${receita:.2f}")

            else:
                print("Opção inválida!")

        elif opcao == "0":
            print("Saindo... Até logo! 👋")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
