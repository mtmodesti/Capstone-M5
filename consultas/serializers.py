from agendas.models import Agenda
from convenios.models import Convenio
from django.shortcuts import get_object_or_404
from medicos.models import Medico
from medicos.serializers import MedicoConsultaSerializer
from pacientes.models import Paciente
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from usuarios.models import Usuario
from usuarios.serializers import ConsultaUsuarioCriadorSerializer
from .models import Consulta
from pacientes.serializers import PacienteConsultaSerializer


class ConsultaSerializer(serializers.ModelSerializer):
    criado_pelo_atendente = ConsultaUsuarioCriadorSerializer(source='usuario', read_only=True)
    data_da_consulta = serializers.DateTimeField(input_formats=['%d-%m-%Y %H:%M',])
    paciente = PacienteConsultaSerializer(read_only=True)
    medico = MedicoConsultaSerializer(read_only=True)
    class Meta:
        model  = Consulta
        fields = [
            "id",
            'criado_pelo_atendente',
            'data_da_consulta',
            'confirmado',
            'compareceu',
            'pago',
            'paciente',
            'medico',
            'criado_em',
            'atualizado_em',
        ]
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
        # convenio_data = validated_data.pop("convenio")
        usuario_data = validated_data.pop("usuario")
        medico_data = validated_data.pop("medico")
        
        paciente = get_object_or_404(Paciente, id = paciente_id)
        # convenio = get_object_or_404(Convenio, id = convenio_data.id)
        medico  = get_object_or_404(Medico, pk = medico_data)
        usuario = get_object_or_404(Usuario, id = usuario_data.id)

        consulta = Consulta.objects.create(
            **validated_data,
            paciente=paciente,
            # convenio=convenio,
            usuario=usuario,
            medico=medico
        )
        Agenda.objects.create(data_consulta=validated_data['data_da_consulta'], medico=medico, consulta=consulta)
        return consulta
        

