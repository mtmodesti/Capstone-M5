from django.db import models

class Medico(models.Model):
    nome          = models.CharField(max_length=127, null=False)
    password      = password.CharField(max_length=127)
    especialidade = models.CharField(max_length=127)
    telefone      = models.CharField(max_length=127)
    email         = models.CharField(max_length=127)
    ativo         = models.BooleanField(default=True, null=False)



