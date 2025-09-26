from cadastro_eventos import CadastroEventos
from inscricoes_participantes import InscricoesParticipantes

if __name__ == "__main__":
    try:
        evento = CadastroEventos(
            nome="Show de Rock",
            data="30/12/2025",
            local="Arena Principal",
            capacidade_maxima=2,
            categoria="Música",
            preco_ingresso=150.0
        )

        p1 = InscricoesParticipantes("Alice", "alice@email.com", evento)
        print(p1)

        p2 = InscricoesParticipantes("Bruno", "bruno@email.com", evento)
        print(p2)

        # Tentativa de e-mail duplicado
        p3 = InscricoesParticipantes("Carlos", "alice@email.com", evento)

    except ValueError as e:
        print("Erro:", e)

    # Tentativa de inscrição acima da capacidade
    try:
        p4 = InscricoesParticipantes("Diana", "diana@email.com", evento)
    except ValueError as e:
        print("Erro:", e)