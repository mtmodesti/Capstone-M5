from django.db import models
import uuid
from agendas.models import Agenda



class Medico(models.Model):

    id                    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nome                  = models.CharField(max_length=127)
    senha              = models.CharField(max_length=127)
    especialidade         = models.CharField(max_length=127)
    registro_profissional = models.CharField(max_length=127, default=None)
    telefone              = models.CharField(max_length=127)
    email                 = models.CharField(max_length=127)
    dias_de_atendimento   = models.DateField(blank=True, default=None)
    ativo                 = models.BooleanField(default=True)
    agente_de_saude = models.BooleanField(default=True)

    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, default = None, null=True)
