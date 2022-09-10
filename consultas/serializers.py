from http.client import FORBIDDEN
from jsonschema import ValidationError
from agendas.models import Agenda
from django.shortcuts import get_object_or_404

from medicos.models import Medico
from medicos.serializers import MedicoConsultaSerializer
from usuarios.serializers import ConsultaUsuarioCriadorSerializer

from pacientes.models import Paciente
from rest_framework import serializers
from usuarios.models import Usuario
from .models import Consulta
from pacientes.serializers import PacienteConsultaSerializer


class ConsultaSerializer(serializers.ModelSerializer):

    paciente = PacienteConsultaSerializer(read_only=True)
    criado_pelo_atendente = ConsultaUsuarioCriadorSerializer(source='usuario', read_only=True)
    medico = MedicoConsultaSerializer(read_only=True)
    
    class Meta:
        model  = Consulta
        fields = [
            "id",
            'descricao',
            'horario',
            'criado_pelo_atendente',
            'confirmado',
            'compareceu',
            'pago',
            'paciente',
            'medico',
            'criado_em',
            'atualizado_em',
            'agenda',
            'consulta_cancelada'
        ]
        depth = 1
        read_only_fields = [
            "id",
            "criado_pelo_atendente",
            "paciente",
            "medico",
            "criado_em",
            "atualizado_em",
        ]


    def create(self, validated_data: dict):
        paciente_id = validated_data.pop("paciente")
        usuario_data = validated_data.pop("usuario")
        medico_data = validated_data.pop("medico")
        horario_agenda_data = validated_data.pop("horario_agenda")
        import ipdb
        paciente = get_object_or_404(Paciente, id = paciente_id)
        medico  = get_object_or_404(Medico, pk = medico_data)
        usuario = get_object_or_404(Usuario, id = usuario_data.id)
        horario_agenda = get_object_or_404(Agenda, pk= horario_agenda_data)

        consulta = Consulta.objects.create(
            **validated_data,
            paciente=paciente,
            usuario=usuario,
            medico=medico,
            agenda=horario_agenda,
            horario=horario_agenda.data_hora_inicial
        )
        
        horario_agenda.agenda = consulta
        horario_agenda.save()
        return consulta
        
        


class ConsultaAgendaSerializer(serializers.ModelSerializer):
    paciente = PacienteConsultaSerializer(read_only=True)
    class Meta:
        model = Consulta
        fields = [
            'id',
            'confirmado',
            'compareceu',
            'pago',
            'criado_em',
            'atualizado_em',
            'paciente',
            'consulta_cancelada'
        ]


