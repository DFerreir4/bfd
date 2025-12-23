import uuid
from django.db import models

class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    endereco = models.TextField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    historico_medico = models.TextField(blank=True)

    def __str__(self):
        return self.nome_completo

