from agendas.serializers import AgendaSerializer
from .models import Medico
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class MedicoSerializer(serializers.ModelSerializer):
    agenda = AgendaSerializer(read_only=True, many=True)
    class Meta:
        model = Medico
        fields = ['especialidade', 'telefone','registro_profissional', 'ativo', 'id', 'agenda']
        extra_kwargs = {
            "agenda": {"read_only": True},
        }

