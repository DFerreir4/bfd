from cadastro_eventos import CadastroEventos

class InscricoesParticipantes:
    def __init__(self, nome: str, email: str, evento: CadastroEventos):
        self.nome = nome
        self.email = email
        self.evento = evento
        self.checkin = False  # por padrão, o participante ainda não fez check-in

        # --- Validação de limite de vagas ---
        if len(self.evento.inscritos) >= self.evento.capacidade_maxima:
            raise ValueError(f"O evento '{self.evento.nome}' já está lotado. Não é possível realizar novas inscrições.")

        # --- Validação de duplicidade de email ---
        for inscrito in self.evento.inscritos:
            if inscrito.email == self.email:
                raise ValueError(f"O e-mail '{self.email}' já está inscrito no evento '{self.evento.nome}'.")

        # Se passou pelas validações, adiciona à lista de inscritos
        self.evento.inscritos.append(self)

    def cancelar_inscricao(self):
        """Cancela a inscrição do participante no evento."""
        if self in self.evento.inscritos:
            self.evento.inscritos.remove(self)
            return f"Inscrição de {self.nome} cancelada com sucesso."
        return f"O participante {self.nome} não está inscrito no evento."

    def realizar_checkin(self):
        """Marca presença no evento."""
        if not self.checkin:
            self.checkin = True
            return f"Check-in realizado para {self.nome}."
        return f"{self.nome} já realizou o check-in."

    def __str__(self):
        status_checkin = "✅ Presente" if self.checkin else "❌ Não fez check-in"
        return f"Participante: {self.nome} | Email: {self.email} | Evento: {self.evento.nome} | {status_checkin}"
