from faker import Faker
import uuid
import random
import cv2
import numpy as np
import os

from django.conf import settings
from pacientes.models import Paciente
from pacientes.models import Paciente
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

fake = Faker('pt_BR')

def gerar_paciente_ficticio():
    sexo = random.choice(['M', 'F', 'O'])

    paciente = Paciente.objects.create(
        id=uuid.uuid4(),
        nome_completo=fake.name(),
        data_nascimento=fake.date_of_birth(
            minimum_age=18,
            maximum_age=90
        ),
        cpf=fake.cpf(),
        sexo=sexo,
        endereco=fake.address(),
        telefone=fake.phone_number(),
        email=fake.unique.email(),
        historico_medico=fake.text(max_nb_chars=300),
    )

    return paciente

def gerar_pacientes_em_lote(quantidade=10):
    pacientes = []

    for _ in range(quantidade):
        pacientes.append(gerar_paciente_ficticio())

    return pacientes

#Gerador de imagem base(gradiente térmico)
def criar_base_termica(largura=256, altura=256):
    gradiente_vertical = np.tile(
        np.linspace(0.4, 0.6, altura),
        (largura, 1)
    ).T

    base = gradiente_vertical * 255
    base = base.astype(np.uint8)

    return base

#Adiciona padrão termico mamário base
def padrao_termico_base(imagem):
    ruido_suave = np.random.normal(0, 5, imagem.shape)
    imagem = imagem + ruido_suave
    imagem = np.clip(imagem, 0, 255)
    return imagem.astype(np.uint8)

#Adicionar anomalias térmicas
#Área circular (nódulo/cisto)
def adicionar_area_circular(imagem, intensidade=40, raio=20):
    h, w = imagem.shape
    centro_x = random.randint(raio, w - raio)
    centro_y = random.randint(raio, h - raio)

    for y in range(h):
        for x in range(w):
            if (x - centro_x)**2 + (y - centro_y)**2 <= raio**2:
                imagem[y, x] += intensidade

    return np.clip(imagem, 0, 255)

#Padrão irregular (maligno)
def adicionar_padrao_irregular(imagem, intensidade=60):
    h, w = imagem.shape
    for _ in range(random.randint(3, 6)):
        x = random.randint(0, w - 1)
        y = random.randint(0, h - 1)
        cv2.circle(imagem, (x, y), random.randint(5, 15), intensidade, -1)
    return np.clip(imagem, 0, 255)

#Ruído gaussiano final
def adicionar_ruido_gaussiano(imagem):
    ruido = np.random.normal(0, 8, imagem.shape)
    imagem = imagem + ruido
    return np.clip(imagem, 0, 255).astype(np.uint8)

#Gerar imagem conforme o tipo clínico
def gerar_imagem_termografia(tipo='saudavel'):
    imagem = criar_base_termica()
    imagem = padrao_termico_base(imagem)

    if tipo == 'benigno':
        imagem = adicionar_area_circular(imagem, intensidade=30, raio=15)

    elif tipo == 'cisto':
        imagem = adicionar_area_circular(imagem, intensidade=20, raio=25)

    elif tipo == 'maligno':
        imagem = adicionar_padrao_irregular(imagem, intensidade=70)

    imagem = adicionar_ruido_gaussiano(imagem)

    imagem_colorida = cv2.applyColorMap(imagem, cv2.COLORMAP_JET)

    return imagem_colorida

#Salvar imagem no disco
def salvar_imagem_termografia(imagem, paciente_id, tipo):
    nome_arquivo = f"{paciente_id}_{tipo}_{uuid.uuid4().hex}.png"
    caminho = os.path.join(
        settings.MEDIA_ROOT,
        'termografias',
        nome_arquivo
    )

    cv2.imwrite(caminho, imagem)
    return caminho

#Gerar imagens para pacientes existentes
def gerar_termografias_para_pacientes(qtd_por_paciente=1):
    pacientes = Paciente.objects.all()
    tipos = ['saudavel', 'benigno', 'cisto', 'maligno']
    imagens_geradas = []

    for paciente in pacientes:
        for _ in range(qtd_por_paciente):
            tipo = random.choice(tipos)
            imagem = gerar_imagem_termografia(tipo)
            caminho = salvar_imagem_termografia(imagem, paciente.id, tipo)

            imagens_geradas.append({
                'paciente': paciente.nome_completo,
                'tipo': tipo,
                'arquivo': caminho
            })

    return imagens_geradas

#Sortear a classificação

CLASSIFICACOES_WEKA = {
    'saudavel': 0.50,   # mais comum
    'benigno':  0.25,
    'cisto':    0.15,
    'maligno':  0.10    # menos comum
}

def sortear_classificacao_weka():
    classes = list(CLASSIFICACOES_WEKA.keys())
    pesos = list(CLASSIFICACOES_WEKA.values())

    return random.choices(classes, weights=pesos, k=1)[0]

#Gerar confiança aleatória 70% a 99%
def gerar_confianca_weka():
    return round(random.uniform(0.70, 0.99), 2)

#Gerar tempo de processamento simulado
def gerar_tempo_processamento():
    return random.randint(10, 120)

#Gerar resposta completa do Weka
def gerar_resposta_weka():
    classificacao = sortear_classificacao_weka()
    confianca = gerar_confianca_weka()
    tempo_processamento = gerar_tempo_processamento()

    resposta = {
        'classificacao': classificacao,
        'confianca': confianca,
        'tempo_processamento_segundos': tempo_processamento,
        'data_execucao': datetime.now()
    }

    return resposta

#Gerar respostas em lote (para testes)
def gerar_respostas_weka_em_lote(quantidade=10):
    respostas = []

    for _ in range(quantidade):
        respostas.append(gerar_resposta_weka())

    return respostas




