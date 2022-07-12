import uuid

from django.db import models


class Paciente(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=30)
    data_nascimento = models.DateTimeField()
    data_cadastro = models.DateTimeField()
    ativo = models.BooleanField(default=True)

    convenio = models.OneToOneField(
        "convenios.Convenio", models.SET_NULL, related_name="paciente", null=True
    )
