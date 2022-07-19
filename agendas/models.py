import uuid
from django.db import models

class Agenda(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    data_consulta = models.CharField(max_length=100)
    medico = models.ForeignKey('medicos.Medico', on_delete=models.CASCADE, related_name='agenda', max_length=255)
    consulta = models.ForeignKey("consultas.Consulta", on_delete=models.CASCADE, related_name='agenda', null=True)
