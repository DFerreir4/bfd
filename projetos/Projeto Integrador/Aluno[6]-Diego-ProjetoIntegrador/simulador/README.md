# 🧪 Simulador de Termografia Mamária com Django

## 📌 Visão Geral do Projeto
Este projeto acadêmico tem como objetivo a criação de um **simulador completo** para testes de sistemas baseados em Django, capaz de:

- Gerar **pacientes fictícios** com dados realistas
- Gerar **imagens simuladas de termografia mamária**
- Simular **classificações automáticas** (estilo WEKA)
- Disponibilizar **endpoints HTTP** para consumo dos dados
- Criar um **comando de gerenciamento** para inicializar dados de teste

---

##  Tecnologias Utilizadas

- Python 3.10+
- Django 5+
- Faker (dados fictícios)
- NumPy (matriz térmica)
- OpenCV (geração de imagens)
- SQLite (banco padrão Django)

---

##  1. Criação do Ambiente (do zero)

### 1.1 Instalar o Python

Baixe em: https://www.python.org/downloads/

 Marque **Add Python to PATH** durante a instalação.

Verifique:
```bash
python --version
```

---

### 1.2 Criar pasta do projeto

```bash
mkdir simulador_django
cd simulador_django
```

---

### 1.3 Criar e ativar ambiente virtual

```bash
python -m venv venv
```

Ativar:

**Windows**
```bash
venv\Scripts\activate
```

**Linux/Mac**
```bash
source venv/bin/activate
```

---

### 1.4 Instalar dependências

```bash
pip install django faker numpy opencv-python
```

---

##  2. Criar Projeto Django

```bash
django-admin startproject core .
python manage.py runserver
```

Acesse:
```
http://127.0.0.1:8000/
```

---

##  3. Criar Apps

```bash
python manage.py startapp simulator
python manage.py startapp pacientes
```

Registrar em `core/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'simulator',
    'pacientes',
]
```

---

## 4. Model de Paciente

Arquivo: `pacientes/models.py`

Campos:
- UUID
- Nome completo
- Data de nascimento
- CPF
- Sexo
- Endereço
- Telefone
- Email
- Histórico médico

Após criar o model:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Serviços de Simulação

Arquivo: `simulator/services.py`

### Funcionalidades:
- Geração de pacientes fictícios (Faker)
- Geração de imagens de termografia
- Simulação de classificações (WEKA)

Essas funções **não são acessadas diretamente**, apenas reutilizadas.

---

## 6. Geração de Imagens de Termografia

As imagens são geradas usando:
- Gradiente térmico
- Anomalias circulares
- Padrões irregulares
- Ruído gaussiano

Tipos simulados:
- saudavel
- benigno
- cisto
- maligno

As imagens são salvas em:
```
/media/termografias/
```

Configuração em `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 🧠 7. Simulação de Classificação (WEKA)

Cada classificação contém:
- Classe prevista
- Confiança (70% a 99%)
- Tempo de processamento (10 a 120s)
- Data de execução

Distribuição probabilística realista:
- Saudável: 50%
- Benigno: 25%
- Cisto: 15%
- Maligno: 10%

---

## 8. Views e Endpoints

Arquivo: `simulator/views.py`

### Endpoints disponíveis:

####  Gerar pacientes
```
GET /simulator/gerar-pacientes/?qtd=5
```

####  Gerar termografias
```
GET /simulator/gerar-termografias/?qtd=1
```

####  Gerar classificação
```
GET /simulator/gerar-classificacao/
```

URLs do app:

Arquivo: `simulator/urls.py`

URLs principais:

Arquivo: `core/urls.py`

---

## 9. Comando de Gerenciamento

Criado comando customizado:

```bash
python manage.py inicializar_dados
```

Com parâmetros:

```bash
python manage.py inicializar_dados --pacientes 10 --termografias 2
```

Esse comando:
- Cria pacientes
- Gera termografias
- Simula classificações

---

## 10. Testes

### Rodar servidor:
```bash
python manage.py runserver
```

### Testar endpoints:
Abra o navegador e acesse:

```
http://127.0.0.1:8000/simulator/gerar-pacientes/
```

---

## Conclusão

Este projeto entrega:
- Simulador completo e funcional
- Estrutura modular
- Código reutilizável
- Ideal para testes

---



