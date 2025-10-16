import json
# importa a biblioteca json que permite transformar dados do Python em texto (e salvar em arquivo)
# e também ler texto de arquivo e transformar de volta em dados do Python.

from datetime import datetime
# importa 'datetime' que serve para trabalhar com datas (dia/mês/ano, comparar datas, etc).

class CadastroEventos:
    # começa a definição da classe CadastroEventos — uma "receita" para criar objetos que representam eventos.
    # dentro dessa classe teremos métodos e atributos para gerenciar os eventos.

    # Lista estática para armazenar todos os eventos criados
    _eventos = []
    # _eventos é uma lista que guarda todos os eventos que foram criados durante a execução do programa.
    # o underline no começo é só uma convenção para dizer "isso é interno da classe".

    _arquivo_dados = "eventos.json"
    # nome do arquivo onde vamos guardar os eventos no formato JSON — assim os dados não se perdem quando fechar o programa.

    def __init__(self, nome: str, data: str, local: str, capacidade_maxima: int, categoria: str, preco_ingresso: float):
        # método construtor: é executado sempre que criamos um novo evento com CadastroEventos(...)
        # recebe os dados que definem o evento: nome, data (texto), local, capacidade máxima, categoria e preço.

        self.nome = nome
        # guarda o nome do evento no objeto (atributo público chamado 'nome')

        self.data = data  # chama o setter
        # aqui usamos o setter da propriedade 'data' (mais abaixo) — ele vai validar o formato e converter para datetime

        self.local = local
        # guarda o local do evento

        self.capacidade_maxima = capacidade_maxima  # chama o setter
        # usa o setter de 'capacidade_maxima' para validar que é um número inteiro positivo

        self.categoria = categoria
        # guarda a categoria do evento (ex: "Filme", "Tecnologia", etc.)

        self.preco_ingresso = preco_ingresso  # chama o setter
        # usa o setter de 'preco_ingresso' para validar que o preço é um número positivo

        self.inscritos = []  # lista de participantes
        # cria uma lista vazia que, depois, vai receber os objetos dos participantes inscritos

        # Adiciona este evento à lista global
        CadastroEventos._eventos.append(self)
        # coloca este novo evento dentro da lista estática _eventos — assim todos os eventos ficam acessíveis globalmente

        self.salvar_eventos_json()  # salva automaticamente a cada novo cadastro
        # salva todos os eventos no arquivo JSON toda vez que um novo evento é criado,
        # assim os dados já ficam persistidos no disco.

    # Validação de data
    @property
    def data(self):
        # getter da propriedade 'data' — permite acessar evento.data e obter o valor (um datetime)
        return self._data

    @data.setter
    def data(self, valor: str):
        # setter da propriedade 'data' — aqui validamos a data antes de salvar no atributo interno _data
        try:
            data_evento = datetime.strptime(valor, "%d/%m/%Y")
            # tenta transformar a string 'valor' no formato "DD/MM/AAAA" em um objeto datetime
        except ValueError:
            raise ValueError("Data INVÁLIDA! Use o formato DD/MM/AAAA.")
            # se a conversão falhar, levanta um erro explicando que o formato está errado

        if data_evento < datetime.now():
            raise ValueError("A data do evento não pode ser anterior à data atual.")
            # se a data for passada (menor que agora), levanta um erro dizendo que não pode ser no passado

        self._data = data_evento
        # se tudo estiver ok, guarda o objeto datetime no atributo privado _data

    #Validação de capacidade máxima
    @property
    def capacidade_maxima(self):
        # getter para capacidade_maxima — retorna o valor guardado
        return self._capacidade_maxima

    @capacidade_maxima.setter
    def capacidade_maxima(self, valor: int):
        # setter que valida se a capacidade é um inteiro maior que zero
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("A capacidade máxima deve ser um número inteiro positivo.")
            # se não for inteiro ou for menor/igual a zero, levanta um erro
        self._capacidade_maxima = valor
        # guarda o valor validado em _capacidade_maxima

    # Validação de preço do ingresso
    @property
    def preco_ingresso(self):
        # getter do preço — retorna o preço guardado
        return self._preco_ingresso

    @preco_ingresso.setter
    def preco_ingresso(self, valor: float):
        # setter do preço com validação
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("O preço do ingresso deve ser um número positivo maior que zero.")
            # se o preço não for número ou for menor/igual a zero, levanta erro
        self._preco_ingresso = float(valor)
        # garante que o valor seja um float e guarda em _preco_ingresso

    # Métodos extras
    @classmethod
    def salvar_eventos_json(cls):
        """Salva todos os eventos e participantes em um arquivo JSON."""
        # método de classe que pega todos os eventos em _eventos e escreve no arquivo JSON
        dados = []
        # cria uma lista vazia que vamos preencher com dicionários (estruturas simples) representando cada evento
        for evento in cls._eventos:
            # percorre cada evento que está na lista _eventos
            dados.append({
                "nome": evento.nome,
                "data": evento.data.strftime("%d/%m/%Y"),
                # salva a data como string no formato DD/MM/AAAA (porque JSON não entende objetos datetime)
                "local": evento.local,
                "capacidade_maxima": evento.capacidade_maxima,
                "categoria": evento.categoria,
                "preco_ingresso": evento.preco_ingresso,
                "inscritos": [
                    {
                        "nome": p.nome,
                        "email": p.email,
                        "checkin": getattr(p, "checkin", False)
                    } for p in evento.inscritos
                    # para cada participante inscrito, guardamos um dicionário com nome, email e se fez check-in
                    # usamos getattr(p, "checkin", False) para garantir que, se o atributo checkin não existir,
                    # o valor padrão será False.
                ]
            })

        with open(cls._arquivo_dados, "w", encoding="utf-8") as f:
            # abre (ou cria) o arquivo 'eventos.json' para escrita usando UTF-8
            json.dump(dados, f, ensure_ascii=False, indent=4)
            # escreve a lista 'dados' no arquivo em formato JSON, com indent=4 para ficar legível

    @classmethod
    def carregar_eventos_json(cls):
        """Carrega os eventos e participantes salvos no arquivo JSON."""
        # tenta ler o arquivo JSON e reconstruir os objetos Evento e Participante na memória
        try:
            with open(cls._arquivo_dados, "r", encoding="utf-8") as f:
                dados = json.load(f)
                # carrega os dados do arquivo e transforma em estruturas Python (listas e dicionários)

            from inscricoes_participantes import InscricoesParticipantes
            # importa a classe InscricoesParticipantes aqui dentro do método para evitar problemas de import circular
            # (ou seja, os arquivos importarem um ao outro no início pode causar erro; importar aqui evita isso).

            cls._eventos = []
            # limpa a lista atual de eventos antes de reconstruí-la a partir do JSON

            for item in dados:
                # para cada dicionário 'item' lido do JSON, criamos um evento novo
                evento = CadastroEventos(
                    item["nome"],
                    item["data"],
                    item["local"],
                    item["capacidade_maxima"],
                    item["categoria"],
                    item["preco_ingresso"]
                )
                # aqui chamamos o construtor normalmente — isso também adiciona o evento em _eventos
                evento.inscritos = []
                # zeramos a lista de inscritos porque vamos recriar os objetos participantes logo abaixo

                for inscrito in item.get("inscritos", []):
                    # percorre a lista de inscritos salva no JSON (se houver)
                    participante = InscricoesParticipantes(
                        inscrito["nome"], inscrito["email"], evento, salvar=False
                    )
                    # cria um objeto InscricoesParticipantes mas com salvar=False para não disparar novo salvamento
                    participante.checkin = inscrito.get("checkin", False)
                    # define se o participante fez check-in usando o que estava salvo no JSON
                    # o método InscricoesParticipantes adiciona o participante em evento.inscritos automaticamente

        except FileNotFoundError:
            cls._eventos = []
            # se o arquivo JSON não existir (primeira execução), inicia a lista de eventos vazia

    @classmethod
    def listar_eventos(cls):
        # Lista todos os eventos cadastrados.
        if not cls._eventos:
            return "Nenhum evento cadastrado."
            # se não houver eventos, retorna uma mensagem amigável
        return "\n\n".join(str(evento) for evento in cls._eventos)
        # caso contrário, transforma cada evento em string (usando __str__) e junta com duas quebras de linha

    @classmethod
    def buscar_eventos(cls, categoria: str = None, data: str = None):
        # Busca eventos por categoria ou data (DD/MM/AAAA).
        resultados = cls._eventos
        # começa com todos os eventos e vai filtrando conforme os parâmetros informados

        if categoria:
            resultados = [e for e in resultados if e.categoria.lower() == categoria.lower()]
            # se a categoria foi informada, filtra os eventos cujo atributo categoria bate (ignorando maiúsculas/minúsculas)

        if data:
            try:
                data_busca = datetime.strptime(data, "%d/%m/%Y")
                # tenta converter a string de busca para um objeto datetime
            except ValueError:
                raise ValueError("Data INVÁLIDA! Use o formato DD/MM/AAAA.")
                # se a data não estiver no formato correto, levanta um erro explicando isso
            resultados = [e for e in resultados if e.data.date() == data_busca.date()]
            # filtra apenas os eventos cuja data (apenas a parte de data) seja igual à data buscada

        return resultados if resultados else "Nenhum evento encontrado."
        # retorna a lista de eventos encontrados ou uma mensagem dizendo que não encontrou nada

    def __str__(self):
        # __str__ define como o objeto será convertido em texto quando usamos print(evento)
        return (f"Evento: {self.nome}\n"
                f"Data: {self.data.strftime('%d/%m/%Y')}\n"
                f"Local: {self.local}\n"
                f"Capacidade Máxima: {self.capacidade_maxima}\n"
                f"Categoria: {self.categoria}\n"
                f"Preço do Ingresso: R${self.preco_ingresso:.2f}\n"
                f"Inscritos: {len(self.inscritos)}/{self.capacidade_maxima}")
        # retorna um texto bonito com as informações do evento, data formatada, preço com duas casas decimais, e número de inscritos
