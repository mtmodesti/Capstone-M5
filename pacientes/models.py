from django.utils import timezone
import uuid

from django.db import models


class Paciente(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField()
    ativo = models.BooleanField(default=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default="Ok")

    convenio = models.ForeignKey(
        "convenios.Convenio", on_delete=models.CASCADE, related_name="paciente", null=True
    )
