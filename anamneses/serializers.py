from rest_framework import serializers

from pacientes.serializers import PacienteSerializer
from .models import Anamnese

class AnamneseSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)
    class Meta:
        model = Anamnese
        fields = ["id", "descricao", "criado_em", "paciente"]