from agendas.serializers import AgendaSerializer
from .models import Medico
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class MedicoSerializer(serializers.ModelSerializer):
    agenda = AgendaSerializer(read_only=True, many=True)
    class Meta:
        model = Medico
        fields = [
            'id',
            'nome',
            'email',
            'especialidade',
            'telefone',
            'registro_profissional',
            'ativo',
            'agenda',
        ]
        extra_kwargs = {
            "agenda": {"read_only": True},
        }


class MedicoConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = [
            'id',
            'nome',
            'email',
            'especialidade',
            'telefone',
            'registro_profissional'
        ]

