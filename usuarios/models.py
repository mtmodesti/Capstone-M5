import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from usuarios.utils import UsuarioCustomizado

# Create your models here.
class Usuario(AbstractUser):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=255)
    nome = models.CharField(max_length=255, unique=True)
    
    username = None
    
    USERNAME_FIELD = "nome"
    
    objects = UsuarioCustomizado()