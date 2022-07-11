import uuid
from django.db import models

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)