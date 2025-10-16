# Importa a classe CadastroEventos, pois precisaremos dela para associar um participante a um evento
from cadastro_eventos import CadastroEventos

# Define a classe que representa a inscrição de um participante em um evento
class InscricoesParticipantes:
    # O método __init__ é o "construtor" da classe — ele roda automaticamente quando criamos um novo participante inscrito
    def __init__(self, nome: str, email: str, evento: CadastroEventos, salvar=True):
        # Guarda o nome do participante
        self.nome = nome
        # Guarda o e-mail do participante (usado como identificador único)
        self.email = email
        # Guarda o evento em que ele está inscrito
        self.evento = evento
        # Define que, por padrão, o participante ainda não fez o check-in
        self.checkin = False  

        #Validação 1: verifica se o evento ainda tem vagas disponíveis
        # Se o número de inscritos for igual ou maior à capacidade máxima, o evento está lotado
        if len(self.evento.inscritos) >= self.evento.capacidade_maxima:
            # Se o evento estiver cheio, é levantado um erro e a inscrição não é feita
            raise ValueError(f"O evento '{self.evento.nome}' já está lotado. NÃO é possível realizar novas inscrições.")

        #Validação 2: verifica se o e-mail já está inscrito no evento
        # Percorre todos os participantes já inscritos nesse evento
        for inscrito in self.evento.inscritos:
            # Compara o e-mail do novo participante com os e-mails existentes
            if inscrito.email == self.email:
                # Se já existir, gera um erro informando que o participante já está inscrito
                raise ValueError(f"O e-mail '{self.email}' já está inscrito no evento '{self.evento.nome}'.")

        # Se passou pelas duas validações, significa que pode se inscrever
        # Adiciona o novo participante à lista de inscritos do evento
        self.evento.inscritos.append(self)

        # Se o parâmetro "salvar" for True, atualiza o arquivo JSON com os dados atualizados
        if salvar:
            CadastroEventos.salvar_eventos_json()

    # Método para cancelar a inscrição do participante
    def cancelar_inscricao(self):
        """Cancela a inscrição do participante no evento."""
        # Verifica se o participante realmente está inscrito no evento
        if self in self.evento.inscritos:
            # Remove o participante da lista de inscritos
            self.evento.inscritos.remove(self)
            # Retorna uma mensagem de confirmação
            return f"Inscrição de {self.nome} cancelada com sucesso."
        # Caso ele não esteja inscrito, mostra uma mensagem informando isso
        return f"O participante {self.nome} NÃO está inscrito no evento."

    #Método para realizar o check-in
    def realizar_checkin(self):
        """Marca presença no evento."""
        # Se o participante ainda não fez check-in
        if not self.checkin:
            # Atualiza o atributo checkin para True (significa que ele compareceu)
            self.checkin = True
            # Retorna uma mensagem de sucesso
            return f"Check-in realizado para {self.nome}."
        # Caso já tenha feito check-in antes, informa isso
        return f"{self.nome} já realizou o check-in."

    # Método para transformar o objeto em texto legível
    def __str__(self):
        # Verifica o status do check-in e guarda uma frase correspondente
        status_checkin = "Fez Check-in" if self.checkin else "Não fez check-in"
        # Retorna uma string bonita com as informações do participante e evento
        return f"Participante: {self.nome} | Email: {self.email} | Evento: {self.evento.nome} | {status_checkin}"
