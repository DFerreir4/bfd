from django.core.management.base import BaseCommand

from simulator.services import (
    gerar_pacientes_em_lote,
    gerar_termografias_para_pacientes,
    gerar_resposta_weka
)

class Command(BaseCommand):
    help = 'Inicializa o banco com dados de teste (pacientes, termografias e classificações)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--pacientes',
            type=int,
            default=5,
            help='Quantidade de pacientes fictícios'
        )

        parser.add_argument(
            '--termografias',
            type=int,
            default=1,
            help='Quantidade de termografias por paciente'
        )

    def handle(self, *args, **options):
        qtd_pacientes = options['pacientes']
        qtd_termografias = options['termografias']

        self.stdout.write(self.style.SUCCESS('🚀 Iniciando geração de dados de teste...'))

        pacientes = gerar_pacientes_em_lote(qtd_pacientes)
        self.stdout.write(self.style.SUCCESS(f'✅ {len(pacientes)} pacientes criados'))

        imagens = gerar_termografias_para_pacientes(qtd_termografias)
        self.stdout.write(self.style.SUCCESS(f'🖼️ {len(imagens)} termografias geradas'))

        # Simular classificações
        self.stdout.write(self.style.SUCCESS('🧠 Gerando classificações simuladas (WEKA)...'))
        for _ in range(len(imagens)):
            gerar_resposta_weka()

        self.stdout.write(self.style.SUCCESS('🎉 Dados de teste gerados com sucesso!'))
