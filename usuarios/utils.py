from django.contrib.auth.models import BaseUserManager
from medicos.models import Medico

class UsuarioCustomizado(BaseUserManager):
    
    def _criar_usuario(self, nome, password, is_superuser, is_staff, agente_de_saude, **extra_fields):
        if not nome:
            raise ValueError({"erro": "O nome não pode ficar vazio"})
        usuario = self.model(
            nome = nome,
            is_active=True,
            is_superuser=is_superuser,
            is_staff=is_staff,
            agente_de_saude=agente_de_saude,
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self.db)
        return usuario

    def criar_usuario(self, nome, password, **extra_fields):
        return self._criar_usuario(nome, password, False, True, False, **extra_fields)
    
    def create_superuser(self, nome, password, **extra_fields):
        return self._criar_usuario(nome, password, True, True, False,**extra_fields)

    def criar_agente_de_saude(self, nome, password, **extra_fields):
        return self._criar_usuario(nome, password, False, False, True, **extra_fields)
