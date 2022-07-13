import uuid
from django.db import models

class Agenda(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    data_consulta = models.DateTimeField()
    medico_id = models.CharField(max_length=255)
