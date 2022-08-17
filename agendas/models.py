import uuid
from django.db import models

class Agenda(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    dia_da_consulta = models.DateField(null=True)
    horario_inicial = models.TimeField(null=True)
    horario_final = models.TimeField(null=True)
    # descricao_da_consulta = models.TextField(default=None, null=True)
    data_hora_inicial = models.DateTimeField(null=True)
    medico = models.ForeignKey(
        'medicos.Medico',
        on_delete=models.CASCADE,
        related_name='agenda',
        max_length=255
    )
    consulta   = models.OneToOneField(
        'consultas.Consulta',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='agenda'
    )