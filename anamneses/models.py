from django.db import models
from datetime import datetime

import uuid

# Create your models here.
class Anamnese(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    descricao = models.CharField(max_length=255)
    criado_em = models.DateTimeField(datetime.now())
    
    paciente = models.ForeignKey("pacientes.Paciente", on_delete=models.CASCADE, related_name="anamnese")