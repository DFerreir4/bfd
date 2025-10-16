import unittest  # importa a biblioteca de testes que vem com o Python
import os        # serve para mexer com arquivos (por exemplo: apagar um .json no começo)
from datetime import datetime, timedelta  # importa funções para trabalhar com datas
from cadastro_eventos import CadastroEventos  # importa a classe que gerencia eventos
from inscricoes_participantes import InscricoesParticipantes  # importa a classe de inscrições


class TestSistemaEventos(unittest.TestCase):
    # Essa classe agrupa vários testes.
    # Cada método que começa com "test_" é um teste que será executado automaticamente.

    def setUp(self):
        """
        O setUp roda antes de cada teste.
        Aqui garantimos que o ambiente está limpo para não misturar resultados.
        """
        CadastroEventos._eventos = []  # limpa a lista de eventos em memória
        # se existir o arquivo JSON gerado por execuções anteriores, exclui para começar limpo
        if os.path.exists(CadastroEventos._arquivo_dados):
            os.remove(CadastroEventos._arquivo_dados)


    def test_validacao_data_invalida(self):
        """
        Teste 1: tenta criar um evento com data no formato errado (ex: '99/99/9999').
        Esperamos que o programa lance um erro (ValueError) porque a data é inválida.
        """
        # with self.assertRaises(ValueError): significa "espero que ocorra esse erro aqui dentro"
        with self.assertRaises(ValueError):
            # tentamos criar um evento com data impossível — isso deve gerar erro
            CadastroEventos("Show", "99/99/9999", "Arena", 100, "Música", 50.0)


    def test_data_passada(self):
        """
        Teste 2: tenta criar um evento com data no passado (ontem).
        O sistema não aceita eventos com data anterior à data de hoje.
        """
        # calcula a data de ontem e transforma em string no formato DD/MM/AAAA
        data_antiga = (datetime.today() - timedelta(days=1)).strftime("%d/%m/%Y")
        # espera que criar com data passada levante ValueError
        with self.assertRaises(ValueError):
            CadastroEventos("Evento Passado", data_antiga, "Praça", 100, "Feira", 20.0)


    def test_criacao_evento_valido(self):
        """
        Teste 3: cria um evento com data futura e dados corretos.
        Verifica se o evento foi adicionado à lista global de eventos.
        """
        # cria uma data 5 dias no futuro
        data_futura = (datetime.today() + timedelta(days=5)).strftime("%d/%m/%Y")
        # cria o evento válido
        evento = CadastroEventos("Cinema", data_futura, "Shopping", 50, "Entretenimento", 25.0)
        # verifica se o evento está na lista _eventos — ou seja, foi cadastrado
        self.assertIn(evento, CadastroEventos._eventos)


    def test_limite_de_vagas(self):
        """
        Teste 4: verifica que o sistema bloqueia inscrições quando a capacidade é atingida.
        Criamos um evento com capacidade 1, inscrevemos um participante com sucesso,
        e tentamos inscrever outro, que deve gerar erro.
        """
        data_futura = (datetime.today() + timedelta(days=5)).strftime("%d/%m/%Y")
        evento = CadastroEventos("Curso Python", data_futura, "Online", 1, "Tecnologia", 30.0)
        # primeira inscrição deve funcionar
        InscricoesParticipantes("João", "joao@email.com", evento)
        # segunda inscrição deve levantar erro, porque capacidade = 1
        with self.assertRaises(ValueError):
            InscricoesParticipantes("Maria", "maria@email.com", evento)


    def test_email_duplicado(self):
        """
        Teste 5: evita que o mesmo e-mail seja inscrito duas vezes no mesmo evento.
        """
        data_futura = (datetime.today() + timedelta(days=5)).strftime("%d/%m/%Y")
        evento = CadastroEventos("Workshop", data_futura, "Auditório", 5, "Educação", 40.0)
        # primeira inscrição com e-mail "pedro@email.com" funciona
        InscricoesParticipantes("Pedro", "pedro@email.com", evento)
        # tentar inscrever novamente com o mesmo e-mail deve gerar erro
        with self.assertRaises(ValueError):
            InscricoesParticipantes("Pedro", "pedro@email.com", evento)


    def test_checkin_realizado(self):
        """
        Teste 6: verifica que o check-in funciona e altera o atributo checkin para True.
        """
        data_futura = (datetime.today() + timedelta(days=5)).strftime("%d/%m/%Y")
        evento = CadastroEventos("Palestra", data_futura, "Teatro", 50, "Cultura", 15.0)
        participante = InscricoesParticipantes("Ana", "ana@email.com", evento)
        # ao chamar realizar_checkin, o método deve retornar a mensagem esperada
        resultado = participante.realizar_checkin()
        self.assertEqual(resultado, "Check-in realizado para Ana.")
        # e o atributo checkin deve estar True
        self.assertTrue(participante.checkin)


    def test_checkin_duplicado(self):
        """
        Teste 7: se o participante tentar fazer check-in duas vezes, a segunda chamada
        deve retornar uma mensagem dizendo que ele já fez check-in.
        """
        data_futura = (datetime.today() + timedelta(days=5)).strftime("%d/%m/%Y")
        evento = CadastroEventos("Palestra 2", data_futura, "Auditório", 100, "Cultura", 10.0)
        participante = InscricoesParticipantes("Bruna", "bruna@email.com", evento)
        participante.realizar_checkin()  # primeiro check-in: ok
        resultado = participante.realizar_checkin()  # segundo: já foi feito
        self.assertEqual(resultado, "Bruna já realizou o check-in.")


    def test_cancelar_inscricao(self):
        """
        Teste 8: verifica que cancelar a inscrição remove o participante da lista do evento.
        """
        data_futura = (datetime.today() + timedelta(days=10)).strftime("%d/%m/%Y")
        evento = CadastroEventos("Seminário", data_futura, "Centro", 20, "Negócios", 100.0)
        participante = InscricoesParticipantes("Carlos", "carlos@email.com", evento)
        mensagem = participante.cancelar_inscricao()
        # checa se a mensagem de retorno é a esperada
        self.assertEqual(mensagem, "Inscrição de Carlos cancelada com sucesso.")
        # e confirma que o participante não está mais na lista de inscritos
        self.assertNotIn(participante, evento.inscritos)


    def test_salvar_e_carregar_json(self):
        """
        Teste 9: verifica que salvar no JSON e depois carregar reconstrói os objetos corretamente.
        Criamos um evento, uma inscrição e um check-in, salvamos, zeramos a memória e carregamos do arquivo.
        """
        data_futura = (datetime.today() + timedelta(days=15)).strftime("%d/%m/%Y")
        evento = CadastroEventos("Feira", data_futura, "Parque", 100, "Cultura", 5.0)
        participante = InscricoesParticipantes("Julia", "julia@email.com", evento)
        participante.realizar_checkin()  # marca presença

        # salva explicitamente (também é salvo no construtor, mas chamamos para garantir)
        CadastroEventos.salvar_eventos_json()
        # limpa a memória para simular reinício do programa
        CadastroEventos._eventos = []
        # carrega do arquivo JSON
        CadastroEventos.carregar_eventos_json()

        # depois de carregar, esperamos 1 evento na lista
        self.assertEqual(len(CadastroEventos._eventos), 1)
        evento_carregado = CadastroEventos._eventos[0]
        # verifica que o nome do evento é o mesmo
        self.assertEqual(evento_carregado.nome, "Feira")
        # verifica que existe 1 inscrito
        self.assertEqual(len(evento_carregado.inscritos), 1)
        # e que esse inscrito tem checkin = True
        self.assertTrue(evento_carregado.inscritos[0].checkin)


# Ponto de entrada para executar os testes manualmente.
if __name__ == "__main__":
    unittest.main()

#Abaixo um passo a passo de como fazer os testes:

"""
1 - Abra o terminal (Prompt de Comando no Windows, Terminal no Mac/Linux).

2 - Vá até a pasta do seu projeto onde estão os arquivos main.py, cadastro_eventos.py, funcoes.py, inscricoes_participantes.py e o novo test_sistema_eventos.py.

    Exemplo no terminal: cd C:\Users\SeuUsuario\meu_projeto ou cd ~/meu_projeto

    Execute os testes com o comando:

    python -m unittest test_sistema_eventos.py -v


    O -v mostra mais detalhes (cada teste com OK ou FAIL).

4 - Ver resultados:

    Se tudo estiver certo, você verá várias linhas terminando com ok e uma linha final dizendo algo como Ran 9 tests in 0.XXXs.

    Se algum teste falhar, verá FAIL ou ERROR e um relatório explicando qual teste falhou e por quê (traceback e mensagem).
"""


