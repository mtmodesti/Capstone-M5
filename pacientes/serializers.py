from django.utils import timezone
from rest_framework import serializers

from .models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = [
            "id",
            "nome",
            "email",
            "cpf",
            "telefone",
            "data_nascimento",
            "convenio",
            "data_cadastro",
            "atualizado_em"
        ]
        depth = 1
        read_only_fields = ["id", "data_cadastro", "atualizado_em"]

    def create(self, validated_data):
        now = timezone.now()
        return Paciente.objects.create(**validated_data, data_cadastro=now)
