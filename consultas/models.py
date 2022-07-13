import uuid

from django.db import models


class Consulta(models.Model):
    id               = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    paciente         = models.ForeignKey('pacientes.Paciente', related_name='consulta', blank=True, null=True, on_delete=models.CASCADE)
    convenio         = models.OneToOneField('convenios.Convenio', related_name='consulta', on_delete=models.CASCADE)
    usuario          = models.ForeignKey('usuarios.Usuario', related_name='consulta', on_delete=models.CASCADE)
    medico           = models.ForeignKey('medicos.Medico', related_name='consulta', on_delete=models.CASCADE)
    
    confirmado       = models.BooleanField(default=False)
    compareceu       = models.BooleanField(default=False)
    pago             = models.BooleanField(default=False)
    data_da_consulta = models.CharField(max_length=100)

    
