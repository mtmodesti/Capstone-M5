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

        extra_kwargs = {"id": {"read_only": True}}
