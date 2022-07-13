from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id" ,"nome", "is_active", "password"]
        
        extra_kwargs = {"password": {"write_only": True}}
    
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "nome": instance.nome,
            "ativo": instance.is_active
        }
    
    def create(self, validated_data):
        return Usuario.objects.criar_usuario(**validated_data)

        