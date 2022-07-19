from rest_framework import serializers
from pacientes.serializers import PacienteSerializer, PacienteAnamneseSerializer
from .models import Anamnese


class AnamneseSerializer(serializers.ModelSerializer):
    paciente = PacienteAnamneseSerializer(read_only=True)
    class Meta:
        model = Anamnese
        fields = ["id", "descricao", "criado_em", "paciente"]


class AnamnesePacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anamnese
        fields = ["id", "descricao", "criado_em"]