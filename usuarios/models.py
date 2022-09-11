import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from usuarios.utils import UsuarioCustomizado


# Create your models here.
class Usuario(AbstractUser):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=255)
    nome = models.CharField(max_length=255)
    agente_de_saude = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, unique=True)
    criado_em = models.DateTimeField(default=timezone.now,  )
    atualizado_em = models.DateTimeField(auto_now=True)
    username = None
    foto_perfil = models.CharField(max_length=400, default=None, null=True)
    REQUIRED_FIELDS = ["nome"]
    USERNAME_FIELD = "email"
    
    objects = UsuarioCustomizado()