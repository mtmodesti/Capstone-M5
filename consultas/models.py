import uuid

from django.db import models


class Consulta(models.Model):
    id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    paciente   = models.ForeignKey('pacientes.Paciente', related_name='consulta', on_delete=models.CASCADE)
    convenio   = models.OneToOneField('convenios.Convenio', related_name='consulta', on_delete=models.CASCADE)
    atendente  = models.ForeignKey('atendentes.Atendente', related_name='consulta', on_delete=models.CASCADE)
    medico     = models.ForeignKey('medicos.Medico', related_name='consulta', on_delete=models.CASCADE)
    
    confirmado = models.BooleanField()
    compareceu = models.BooleanField()
    pago       = models.BooleanField()
