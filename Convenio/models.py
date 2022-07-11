from django.db import models


class Convenio(models.Model):
    tipo = models.CharField(max_length=127, null=False)