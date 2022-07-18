from django.db import models
import uuid
from agendas.models import Agenda


class Medico(models.Model):

    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nome          = models.CharField(max_length=127, null=True)
    email         = models.CharField(max_length=127, null=True)
    especialidade = models.CharField(max_length=127)
    telefone      = models.CharField(max_length=127)
    ativo         = models.BooleanField(default=True)
    usuario       = models.OneToOneField('usuarios.Usuario', default=None, editable=False, on_delete=models.CASCADE, related_name="medico")
    # agenda        = models.ForeignKey(Agenda, on_delete=models.CASCADE, default=None, null=True)
    registro_profissional = models.CharField(max_length=127, unique=True, default=None)
