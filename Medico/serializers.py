from .models import Medico
from rest_framework import serializers

class MedicoSerializer(serializers.Serializer):
    id             = serializers.CharField(read_only=True)
    password       = serializers.CharField(max_length=127)
    especialidade  = serializers.CharField(max_length=127)
    telefone       = serializers.CharField(max_length=127)
    email          = serializers.EmailField(required=True)
    ativo          = serializers.IntegerField(read_only=True)

