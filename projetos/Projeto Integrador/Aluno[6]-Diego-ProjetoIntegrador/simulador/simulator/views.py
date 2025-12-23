from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from simulator.services import (
    gerar_pacientes_em_lote,
    gerar_termografias_para_pacientes,
    gerar_resposta_weka
)

#view para gerar pacientes fictícios
@require_http_methods(["GET"])
def gerar_pacientes_view(request):
    quantidade = int(request.GET.get('qtd', 5))

    pacientes = gerar_pacientes_em_lote(quantidade)

    return JsonResponse({
        'status': 'sucesso',
        'quantidade_criada': len(pacientes),
        'pacientes': [
            {
                'id': str(p.id),
                'nome': p.nome_completo,
                'email': p.email
            } for p in pacientes
        ]
    })

#View para gerar termografias
@require_http_methods(["GET"])
def gerar_termografias_view(request):
    qtd_por_paciente = int(request.GET.get('qtd', 1))

    imagens = gerar_termografias_para_pacientes(qtd_por_paciente)

    return JsonResponse({
        'status': 'sucesso',
        'total_imagens': len(imagens),
        'imagens': imagens
    })

#view para gerar resposta WEKA
@require_http_methods(["GET"])
def gerar_classificacao_view(request):
    resposta = gerar_resposta_weka()

    return JsonResponse({
        'status': 'sucesso',
        'resultado': resposta
    })

