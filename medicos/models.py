from django.db import models
import uuid


class Medico(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nome          = models.CharField(max_length=127)
    password      = models.CharField(max_length=127)
    especialidade = models.CharField(max_length=127)
    telefone      = models.CharField(max_length=127)
    email         = models.CharField(max_length=127)
    ativo         = models.BooleanField(default=True)

    



