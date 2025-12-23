from django.urls import path
from simulator import views

urlpatterns = [
    path('gerar-pacientes/', views.gerar_pacientes_view, name='gerar_pacientes'),
    path('gerar-termografias/', views.gerar_termografias_view, name='gerar_termografias'),
    path('gerar-classificacao/', views.gerar_classificacao_view, name='gerar_classificacao'),
]
