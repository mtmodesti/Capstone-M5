from django.utils import timezone
from rest_framework import serializers

from .models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = [
            "id",
            "nome",
            "cpf",
            "telefone",
            "data_nascimento",
            "data_cadastro",
            "convenio",
        ]
        depth = 1
        read_only_fields = ["id", "data_cadastro"]

    def create(self, validated_data):
        now = timezone.now()
        return Paciente.objects.create(**validated_data, data_cadastro=now)
