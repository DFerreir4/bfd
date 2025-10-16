from cadastro_eventos import CadastroEventos  # importa a classe CadastroEventos do arquivo cadastro_eventos.py (para criar e acessar eventos)
from inscricoes_participantes import InscricoesParticipantes  # importa a classe InscricoesParticipantes (para inscrever, cancelar, check-in)
from funcoes import *  # importa todas as funções do arquivo funcoes.py (limpar_tela, validar_texto, pausar, etc.)

def menu():  # define a função principal chamada "menu" — onde o programa mostra as opções para o usuário
    while True:  # inicia um laço infinito que mantém o menu aparecendo até o usuário escolher sair
        print("#"*30)  # imprime 30 vezes o caractere '#' — serve para desenhar uma linha visual no terminal
        print("#"*6," MENU PRINCIPAL ","#"*6)  # imprime um cabeçalho "MENU PRINCIPAL" com '#' ao redor para destaque
        print("#"*30)  # outra linha de '#' para fechar o cabeçalho visual
        print("| 1 - Cadastrar evento       |")  # opção 1: cadastrar um novo evento
        print("| 2 - Listar eventos         |")  # opção 2: mostrar todos os eventos cadastrados
        print("| 3 - Inscrever participante |")  # opção 3: inscrever uma pessoa em um evento
        print("| 4 - Realizar check-in      |")  # opção 4: marcar presença (check-in) de um participante
        print("| 5 - Cancelar inscrição     |")  # opção 5: cancelar inscrição de um participante
        print("| 6 - Relatórios             |")  # opção 6: entrar no menu de relatórios
        print("| 0 - Sair                   |")  # opção 0: sair do programa
        print("-"*30)  # imprime uma linha com '-' para separar o menu do input
        opcao = input("\nEscolha uma opção: ")  # lê do teclado qual opção o usuário escolheu e guarda em 'opcao'

        if opcao == "1":  # se o usuário digitou "1", entra no fluxo de cadastrar evento
            while True:  # loop para permitir cadastrar vários eventos seguidos até o usuário decidir parar
                try:  # bloco try para capturar erros e mostrar mensagem amigável ao usuário
                    print("\n")  # pula uma linha para espaçamento visual
                    print("#"*7,"CADASTRAR EVENTO","#"*7)  # cabeçalho do processo de cadastro
                    nome = validar_texto("Nome do evento")  # pede e valida o nome do evento (não pode ficar vazio)
                    data = validar_data("Data do evento")  # pede e valida a data (formato DD/MM/AAAA e não pode ser passada)
                    local = validar_texto("Local do evento")  # pede e valida o local (não pode ficar vazio)
                    capacidade = validar_inteiro("Capacidade máxima")  # pede e valida que a capacidade seja inteiro positivo
                    categoria = validar_texto("Categoria")  # pede e valida a categoria (não pode ficar vazia)
                    
                    # Validação e formatação do preço no campo preço
                    while True:  # loop até o usuário digitar um preço válido
                        preco_input = input("Preço R$(##,##): ").replace(",", ".").strip()  # pede preço, troca vírgula por ponto e tira espaços
                        try:
                            preco = float(preco_input)  # tenta converter o texto para número decimal (float)
                            if preco <= 0:  # valida que o preço seja maior que zero
                                input("ERRO: O preço deve ser maior que zero. Pressione ENTER para tentar novamente.")  # avisa e pede ENTER para repetir
                            else:
                                break  # preço válido → sai do loop
                        except ValueError:
                            input("ERRO: O valor deve ser numérico no formato R$(##,##). Pressione ENTER para tentar novamente.")  # se não for número, mostra erro e repete

                    # VERIFICAÇÃO DE EVENTO DUPLICADO
                    evento_existente = any(  # any(...) retorna True se algum evento da lista já for igual aos dados atuais
                        e.nome.lower() == nome.lower() and  # compara nome ignorando maiúsculas/minúsculas
                        e.data.strftime("%d/%m/%Y") == data and  # compara a data (formatada em string DD/MM/AAAA)
                        e.local.lower() == local.lower() and  # compara local ignorando maiúsculas/minúsculas
                        e.capacidade_maxima == capacidade and  # compara capacidade numérica
                        e.categoria.lower() == categoria.lower() and  # compara categoria ignorando case
                        abs(e.preco_ingresso - preco) < 0.01  # compara preços com pequena tolerância (evita problemas de ponto flutuante)
                        for e in CadastroEventos._eventos  # percorre todos os eventos já cadastrados
                    )

                    if evento_existente:  # se já existir evento igual
                        input("\nNão é possível cadastrar! Esse cadastro já existe. Pressione ENTER para voltar.")  # avisa o usuário
                        limpar_tela()  # limpa a tela para voltar ao menu
                        break  # sai do loop de cadastro (volta ao menu principal)


                    evento = CadastroEventos(nome, data, local, capacidade, categoria, preco)  # cria o objeto evento chamando o construtor
                    print(f"\nEvento '{evento.nome}' cadastrado com SUCESSO!")  # confirma o cadastro para o usuário
                except Exception as e:
                    input(f"Erro: {e}. Pressione ENTER para tentar novamente.")  # em caso de erro qualquer, mostra mensagem e permite tentar de novo

                escolha = input("\nDeseja cadastrar outro evento? (s/n): ").strip().lower()  # pergunta se o usuário quer cadastrar mais um
                if escolha != "s":  # se a resposta não for 's' (sim)
                    limpar_tela()  # limpa a tela
                    break  # sai do loop de cadastro e volta ao menu

        elif opcao == "2":  # LISTAR EVENTOS
            print("\n#### LISTA DE EVENTOS ####")  # título da seção
            print(CadastroEventos.listar_eventos())  # chama o método que retorna a lista formatada de eventos e imprime na tela

            escolha = input("\nVocê deseja fazer uma busca de evento por categoria ou data? (s/n): ").strip().lower()  # pergunta se quer buscar
            if escolha == "s":
                termo = input("Digite a categoria ou a data (DD/MM/AAAA): ").strip()  # pede o termo (categoria ou data)
                
                resultados = []  # cria uma lista vazia para armazenar eventos que batem com a busca
                for evento in CadastroEventos._eventos:  # percorre todos os eventos cadastrados
                    # Verifica se a categoria é igual (ignorando maiúsculas/minúsculas)
                    if evento.categoria.lower() == termo.lower():
                        resultados.append(evento)  # se a categoria bate, adiciona o evento nos resultados
                        continue  # pula para o próximo evento (não precisa checar a data nesse caso)

                    # Verifica se o termo é uma data válida e compara com a data do evento
                    try:
                        termo_data = datetime.strptime(termo, "%d/%m/%Y").date()  # tenta transformar o termo em data (DD/MM/AAAA)
                        if evento.data.date() == termo_data:  # compara as datas (objeto datetime) corretamente
                            resultados.append(evento)  # se a data bate, adiciona o evento nos resultados
                    except ValueError:
                        pass  # se o termo não for uma data, ignora esse erro e continua (pois pode ter sido uma categoria)

                if resultados:  # se a lista de resultados não estiver vazia
                    print("\n#### RESULTADOS DA BUSCA ####")  # título do bloco de resultados
                    for evento in resultados:  # imprime cada evento encontrado em um formato legível
                        print(f"Evento: {evento.nome}")
                        print(f"Data: {evento.data.strftime('%d/%m/%Y')}")
                        print(f"Local: {evento.local}")
                        print(f"Capacidade Máxima: {evento.capacidade_maxima}")
                        print(f"Categoria: {evento.categoria}")
                        print(f"Preço do Ingresso: R${evento.preco_ingresso:.2f}")
                        print(f"Inscritos: {len(evento.inscritos)}\n")
                else:
                    print("\nNenhum evento encontrado.")  # se nada foi achado, mostra essa mensagem
                pausar()  # pede para o usuário pressionar ENTER e limpa a tela depois
            else:
                limpar_tela()  # se o usuário não quiser buscar, limpa a tela e volta ao menu

        elif opcao == "3":  # INSCREVER PARTICIPANTE
            while True:  # loop para permitir várias inscrições seguidas
                try:
                    if not CadastroEventos._eventos:  # se não existir nenhum evento cadastrado
                        print("Nenhum evento cadastrado.")  # avisa ao usuário
                        pausar()  # pausa para o usuário ler e limpa a tela em seguida
                        break  # volta ao menu principal

                    print("\n#### EVENTOS DISPONÍVEIS ####")  # mostra título
                    for i, evento in enumerate(CadastroEventos._eventos, start=1):  # lista os eventos com números
                        print(f"{i} - {evento.nome} ({len(evento.inscritos)}/{evento.capacidade_maxima} vagas)")  # exibe nome e vagas ocupadas/total

                    escolha = validar_inteiro("Escolha o número do evento") - 1  # pede o número do evento e converte para índice da lista (0-based)
                    if escolha < 0 or escolha >= len(CadastroEventos._eventos):  # checa se o índice é válido
                        input("Evento INVÁLIDO. Pressione ENTER para tentar novamente.")  # mensagem de erro
                        continue  # volta ao começo do loop para tentar novamente

                    evento = CadastroEventos._eventos[escolha]  # pega o evento escolhido

                    nome = validar_texto("Nome do participante")  # pede nome do participante
                    email = validar_texto("E-mail do participante")  # pede e valida e-mail (a função só garante que não esteja vazio)

                    participante = InscricoesParticipantes(nome, email, evento)  # tenta criar a inscrição (pode lançar erro se duplicado ou lotado)
                    print(f"\nInscrição de {participante.nome} realizada com SUCESSO!")  # confirma inscrição
                except Exception as e:
                    input(f"Erro: {e}. Pressione ENTER para tentar novamente.")  # mostra erro ocorrido e espera ENTER

                nova_inscricao = input("\nVocê deseja inscrever mais um participante? (s/n): ").strip().lower()  # pergunta se quer inscrever outro
                if nova_inscricao != "s":
                    limpar_tela()  # limpa a tela se não quiser continuar
                    break  # sai do loop e volta ao menu

        elif opcao == "4":  # REALIZAR CHECK-IN
            while True:  # loop para permitir múltiplos check-ins seguidos
                try:
                    email = validar_texto("Digite o e-mail do participante")  # pede o e-mail (não deixa em branco)
                    encontrado = False  # flag para dizer se achou o participante
                    for evento in CadastroEventos._eventos:  # percorre todos os eventos
                        for inscrito in evento.inscritos:  # percorre todos os inscritos de cada evento
                            if inscrito.email == email:  # se o e-mail bater com o inscrito atual
                                print(inscrito.realizar_checkin())  # chama o método que marca o check-in (ou avisa se já foi feito)
                                encontrado = True  # marca que encontrou
                                break  # sai do laço interno (não precisamos procurar mais nesse evento)
                    if not encontrado:
                        print("Participante NÃO encontrado.")  # se depois de tudo não achou, avisa
                except Exception as e:
                    input(f"Erro: {e}. Pressione ENTER para tentar novamente.")  # em caso de erro qualquer, mostra mensagem

                mais_checkin = input("\nVocê deseja fazer mais algum Check-in? (s/n): ").strip().lower()  # pergunta se quer fazer outro check-in
                if mais_checkin != "s":
                    limpar_tela()  # limpa a tela e volta ao menu
                    break  # sai do loop de check-in

        elif opcao == "5":  # CANCELAR INSCRIÇÃO
            while True:  # loop para permitir cancelamentos múltiplos
                try:
                    email = validar_texto("Digite o e-mail do participante")  # pede e valida e-mail
                    encontrado = False  # flag para encontrar inscrição
                    for evento in CadastroEventos._eventos:  # percorre eventos
                        for inscrito in evento.inscritos:  # percorre inscritos do evento
                            if inscrito.email == email:  # se encontrar o e-mail correspondente
                                print(inscrito.cancelar_inscricao())  # chama o método que remove a inscrição e exibe mensagem
                                encontrado = True  # encontrou a inscrição
                                break  # sai do laço interno
                    if not encontrado:
                        print("Participante NÃO encontrado.")  # se não achou nenhum inscrito com esse e-mail, avisa
                except Exception as e:
                    input(f"Erro: {e}. Pressione ENTER para tentar novamente.")  # em caso de erro na operação, mostra mensagem

                mais_cancelar = input("\nVocê deseja cancelar mais uma inscrição? (s/n): ").strip().lower()  # pergunta se quer cancelar outro
                if mais_cancelar != "s":
                    limpar_tela()  # limpa a tela se não quiser continuar cancelando
                    break  # sai do loop de cancelamento

        elif opcao == "6":  # RELATÓRIOS
            limpar_tela()  # limpa a tela antes de mostrar o menu de relatórios para ficar mais limpo
            relatorios()  # chama a função relatorios() que está no módulo funcoes.py

        elif opcao == "0":  # SAIR
            print("Obrigado por ter utilizado nosso sistema. Até a próxima.")  # mensagem de despedida
            break  # sai do loop principal e encerra a função menu (terminando o programa)

        else:  # CASO INVÁLIDO
            input("Opção INVÁLIDA, pressione ENTER para tentar novamente.")  # avisa que a opção não existe
            limpar_tela()  # limpa a tela para mostrar o menu novamente

if __name__ == "__main__":  # se este arquivo for executado diretamente (não importado), executa o bloco abaixo
    limpar_tela()  # limpa a tela antes de começar
    CadastroEventos.carregar_eventos_json()  # carrega eventos salvos anteriormente do arquivo JSON para a memória
    menu()  # chama a função menu() para iniciar a interface com o usuário
