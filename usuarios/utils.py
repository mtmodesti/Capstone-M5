from django.contrib.auth.models import BaseUserManager

class UsuarioCustomizado(BaseUserManager):
    
    def _criar_usuario(self, nome, password, is_superuser, **extra_fields):
        if not nome:
            raise ValueError({"erro": "O nome não pode ficar vazio"})
        
        usuario = self.model(
            nome = nome,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields
        )
        
        usuario.set_password(password)
        
        usuario.save(using=self.db)
        
        return usuario
    
    def criar_usuario(self, nome, password, **extra_fields):
        return self._criar_usuario(nome, password, False, **extra_fields)
    
    def create_superuser(self, nome, password, **extra_fields):
        return self._criar_usuario(nome, password, True, **extra_fields)

