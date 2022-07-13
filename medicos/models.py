from django.db import models
import uuid
from agendas.models import Agenda
from usuarios.models import Usuario


class Medico(models.Model):

    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    especialidade = models.CharField(max_length=127)
    telefone      = models.CharField(max_length=127)
    ativo         = models.BooleanField(default=True)
    usuario       = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="medico")
    agenda        = models.ForeignKey(Agenda, on_delete=models.CASCADE, default = None)
