from cadastro_eventos import CadastroEventos #importa metódos cadastros_eventos
from inscricoes_participantes import InscricoesParticipantes #importa metódos de inscricoes_participantes
from funcoes import *  # importa todas as funções

def menu():
    while True:
        print("#"*30)
        print("#"*6," MENU PRINCIPAL ","#"*6)
        print("#"*30)
        print("| 1 - Cadastrar evento       |")
        print("| 2 - Listar eventos         |")
        print("| 3 - Inscrever participante |")
        print("| 4 - Realizar check-in      |")
        print("| 5 - Cancelar inscrição     |")
        print("| 6 - Relatórios             |")
        print("| 0 - Sair                   |")
        print("-"*30)
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":  # CADASTRAR EVENTO 
            while True:
                try:
                    print("\n")
                    print("#"*7,"CADASTRAR EVENTO","#"*7)
                    nome = validar_texto("Nome do evento")
                    data = validar_data("Data do evento")
                    local = validar_texto("Local do evento")
                    capacidade = validar_inteiro("Capacidade máxima")
                    categoria = validar_texto("Categoria")
                    
                    # Validação e formatação do preço no campo preço
                    while True:
                        preco_input = input("Preço R$(##,##): ").replace(",", ".").strip()
                        try:
                            preco = float(preco_input)
                            if preco <= 0:
                                input("ERRO: O preço deve ser maior que zero. Pressione ENTER para tentar novamente.")
                            else:
                                break
                        except ValueError:
                            input("ERRO: O valor deve ser numérico no formato R$(##,##). Pressione ENTER para tentar novamente.")

                    # --- VERIFICAÇÃO DE EVENTO DUPLICADO ---
                    evento_existente = any(
                        e.nome.lower() == nome.lower() and
                        e.data.strftime("%d/%m/%Y") == data and
                        e.local.lower() == local.lower() and
                        e.capacidade_maxima == capacidade and
                        e.categoria.lower() == categoria.lower() and
                        abs(e.preco_ingresso - preco) < 0.01
                        for e in CadastroEventos._eventos
                    )

                    if evento_existente:
                        input("\nNão é possível cadastrar! Esse cadastro já existe. Pressione ENTER para voltar.")
                        limpar_tela()
                        break


                    evento = CadastroEventos(nome, data, local, capacidade, categoria, preco)
                    print(f"\nEvento '{evento.nome}' cadastrado com SUCESSO!")
                except Exception as e:
                    input(f"Erro: {e}. Pressione ENTER para tentar novamente.")

                escolha = input("\nDeseja cadastrar outro evento? (s/n): ").strip().lower()
                if escolha != "s":
                    limpar_tela()
                    break

        elif opcao == "2":  # LISTAR EVENTOS
            print("\n#### LISTA DE EVENTOS ####")
            print(CadastroEventos.listar_eventos())

            escolha = input("\nVocê deseja fazer uma busca de evento por categoria ou data? (s/n): ").strip().lower()
            if escolha == "s":
                termo = input("Digite a categoria ou a data (DD/MM/AAAA): ").strip()
                
                resultados = []
                for evento in CadastroEventos._eventos:
                    # Verifica se a categoria é igual (ignorando maiúsculas/minúsculas)
                    if evento.categoria.lower() == termo.lower():
                        resultados.append(evento)
                        continue  # já achou, não precisa comparar data

                    # Verifica se o termo é uma data válida e compara com a data do evento
                    try:
                        termo_data = datetime.strptime(termo, "%d/%m/%Y").date()
                        if evento.data.date() == termo_data:
                            resultados.append(evento)
                    except ValueError:
                        pass  # ignora se o termo não for uma data válida

                if resultados:
                    print("\n#### RESULTADOS DA BUSCA ####")
                    for evento in resultados:
                        print(f"Evento: {evento.nome}")
                        print(f"Data: {evento.data.strftime('%d/%m/%Y')}")
                        print(f"Local: {evento.local}")
                        print(f"Capacidade Máxima: {evento.capacidade_maxima}")
                        print(f"Categoria: {evento.categoria}")
                        print(f"Preço do Ingresso: R${evento.preco_ingresso:.2f}")
                        print(f"Inscritos: {len(evento.inscritos)}\n")
                else:
                    print("\nNenhum evento encontrado.")
                pausar()
            else:
                limpar_tela()

        elif opcao == "3":  # INSCREVER PARTICIPANTE
            while True:
                try:
                    if not CadastroEventos._eventos:
                        print("Nenhum evento cadastrado.")
                        pausar()
                        break

                    print("\n#### EVENTOS DISPONÍVEIS ####")
                    for i, evento in enumerate(CadastroEventos._eventos, start=1):
                        print(f"{i} - {evento.nome} ({len(evento.inscritos)}/{evento.capacidade_maxima} vagas)")

                    escolha = validar_inteiro("Escolha o número do evento") - 1
                    if escolha < 0 or escolha >= len(CadastroEventos._eventos):
                        input("Evento INVÁLIDO. Pressione ENTER para tentar novamente.")
                        continue

                    evento = CadastroEventos._eventos[escolha]

                    nome = validar_texto("Nome do participante")
                    email = validar_texto("E-mail do participante")

                    participante = InscricoesParticipantes(nome, email, evento)
                    print(f"\nInscrição de {participante.nome} realizada com SUCESSO!")
                except Exception as e:
                    input(f"Erro: {e}. Pressione ENTER para tentar novamente.")

                nova_inscricao = input("\nVocê deseja inscrever mais um participante? (s/n): ").strip().lower()
                if nova_inscricao != "s":
                    limpar_tela()
                    break

        elif opcao == "4":  # REALIZAR CHECK-IN
            while True:
                try:
                    email = validar_texto("Digite o e-mail do participante")
                    encontrado = False
                    for evento in CadastroEventos._eventos:
                        for inscrito in evento.inscritos:
                            if inscrito.email == email:
                                print(inscrito.realizar_checkin())
                                encontrado = True
                                break
                    if not encontrado:
                        print("Participante NÃO encontrado.")
                except Exception as e:
                    input(f"Erro: {e}. Pressione ENTER para tentar novamente.")

                mais_checkin = input("\nVocê deseja fazer mais algum Check-in? (s/n): ").strip().lower()
                if mais_checkin != "s":
                    limpar_tela()
                    break

        elif opcao == "5":  # CANCELAR INSCRIÇÃO
            while True:
                try:
                    email = validar_texto("Digite o e-mail do participante")
                    encontrado = False
                    for evento in CadastroEventos._eventos:
                        for inscrito in evento.inscritos:
                            if inscrito.email == email:
                                print(inscrito.cancelar_inscricao())
                                encontrado = True
                                break
                    if not encontrado:
                        print("Participante NÃO encontrado.")
                except Exception as e:
                    input(f"Erro: {e}. Pressione ENTER para tentar novamente.")

                mais_cancelar = input("\nVocê deseja cancelar mais uma inscrição? (s/n): ").strip().lower()
                if mais_cancelar != "s":
                    limpar_tela()
                    break

        elif opcao == "6":  # RELATÓRIOS
            limpar_tela()
            relatorios()

        elif opcao == "0":
            print("Obrigado por ter utilizado nosso sistema. Até a próxima.")
            break

        else:
            input("Opção INVÁLIDA, pressione ENTER para tentar novamente.")
            limpar_tela()

if __name__ == "__main__":
    limpar_tela()
    CadastroEventos.carregar_eventos_json()
    menu()
