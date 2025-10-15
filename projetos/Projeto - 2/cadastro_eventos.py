import json
from datetime import datetime

class CadastroEventos:
    # Lista estática para armazenar todos os eventos criados
    _eventos = []
    _arquivo_dados = "eventos.json"

    def __init__(self, nome: str, data: str, local: str, capacidade_maxima: int, categoria: str, preco_ingresso: float):
        self.nome = nome
        self.data = data  # chama o setter
        self.local = local
        self.capacidade_maxima = capacidade_maxima  # chama o setter
        self.categoria = categoria
        self.preco_ingresso = preco_ingresso  # chama o setter
        self.inscritos = []  # lista de participantes

        # Adiciona este evento à lista global
        CadastroEventos._eventos.append(self)
        self.salvar_eventos_json()  # salva automaticamente a cada novo cadastro

    # Validação de data
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, valor: str):
        try:
            data_evento = datetime.strptime(valor, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Data INVÁLIDA! Use o formato DD/MM/AAAA.")

        if data_evento < datetime.now():
            raise ValueError("A data do evento não pode ser anterior à data atual.")

        self._data = data_evento

    #Validação de capacidade máxima
    @property
    def capacidade_maxima(self):
        return self._capacidade_maxima

    @capacidade_maxima.setter
    def capacidade_maxima(self, valor: int):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("A capacidade máxima deve ser um número inteiro positivo.")
        self._capacidade_maxima = valor

    # Validação de preço do ingresso
    @property
    def preco_ingresso(self):
        return self._preco_ingresso

    @preco_ingresso.setter
    def preco_ingresso(self, valor: float):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("O preço do ingresso deve ser um número positivo maior que zero.")
        self._preco_ingresso = float(valor)

    # Métodos extras
    @classmethod
    def salvar_eventos_json(cls):
        """Salva todos os eventos e participantes em um arquivo JSON."""
        dados = []
        for evento in cls._eventos:
            dados.append({
                "nome": evento.nome,
                "data": evento.data.strftime("%d/%m/%Y"),
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
                ]
            })

        with open(cls._arquivo_dados, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    @classmethod
    def carregar_eventos_json(cls):
        """Carrega os eventos e participantes salvos no arquivo JSON."""
        try:
            with open(cls._arquivo_dados, "r", encoding="utf-8") as f:
                dados = json.load(f)

            from inscricoes_participantes import InscricoesParticipantes

            cls._eventos = []
            for item in dados:
                evento = CadastroEventos(
                    item["nome"],
                    item["data"],
                    item["local"],
                    item["capacidade_maxima"],
                    item["categoria"],
                    item["preco_ingresso"]
                )
                evento.inscritos = []
                for inscrito in item.get("inscritos", []):
                    participante = InscricoesParticipantes(
                        inscrito["nome"], inscrito["email"], evento, salvar=False
                    )
                    participante.checkin = inscrito.get("checkin", False)

        except FileNotFoundError:
            cls._eventos = []

    @classmethod
    def listar_eventos(cls):
        # Lista todos os eventos cadastrados.
        if not cls._eventos:
            return "Nenhum evento cadastrado."
        return "\n\n".join(str(evento) for evento in cls._eventos)

    @classmethod
    def buscar_eventos(cls, categoria: str = None, data: str = None):
        # Busca eventos por categoria ou data (DD/MM/AAAA).
        resultados = cls._eventos

        if categoria:
            resultados = [e for e in resultados if e.categoria.lower() == categoria.lower()]

        if data:
            try:
                data_busca = datetime.strptime(data, "%d/%m/%Y")
            except ValueError:
                raise ValueError("Data INVÁLIDA! Use o formato DD/MM/AAAA.")
            resultados = [e for e in resultados if e.data.date() == data_busca.date()]

        return resultados if resultados else "Nenhum evento encontrado."

    def __str__(self):
        return (f"Evento: {self.nome}\n"
                f"Data: {self.data.strftime('%d/%m/%Y')}\n"
                f"Local: {self.local}\n"
                f"Capacidade Máxima: {self.capacidade_maxima}\n"
                f"Categoria: {self.categoria}\n"
                f"Preço do Ingresso: R${self.preco_ingresso:.2f}\n"
                f"Inscritos: {len(self.inscritos)}/{self.capacidade_maxima}")
