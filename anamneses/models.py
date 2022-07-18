from django.db import models
from datetime import datetime
from django.utils import timezone

import uuid

# Create your models here.
class Anamnese(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    descricao = models.CharField(max_length=255)
    criado_em = models.DateTimeField(default=timezone.now, editable=False)
    atualizado_em = models.DateTimeField(auto_now=True)
    paciente = models.ForeignKey("pacientes.Paciente", on_delete=models.CASCADE, related_name="anamnese")