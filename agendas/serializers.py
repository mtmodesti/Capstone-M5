from rest_framework import serializers
from datetime import datetime
from consultas.serializers import ConsultaAgendaSerializer
from .models import Agenda
from rest_framework.exceptions import APIException
from .exceptions import HorarioInicialMaiorQueFinalException, HorarioOcupadoException, HorarioNoPassadoException


class AgendaSerializer(serializers.ModelSerializer):
    horario_disponivel_para_marcar = serializers.SerializerMethodField()
    horario_marcado = serializers.SerializerMethodField()
    horario_passou = serializers.SerializerMethodField()
    consulta = ConsultaAgendaSerializer(read_only=True)
    class Meta:
        model = Agenda
        fields = [
            "id",
            'data_hora_inicial',
            "dia_da_consulta",
            "horario_inicial",
            "horario_final",
            "horario_disponivel_para_marcar",
            "horario_marcado",
            'horario_passou',
            "consulta",
        ]
        depth = 1
        extra_kwargs = {
            "id": {"read_only": True},
            "consulta": {"read_only": True},
            "horario_passou": {"read_only": True},
            "data_hora_inicial": {"read_only": True},
        }
    def get_horario_marcado(self, agenda):
        return agenda.consulta is not None

    def get_horario_passou(self, agenda):
        now = datetime.now()
        data_hora_inicio_str = f'{agenda.dia_da_consulta} {agenda.horario_inicial}'
        data_hora_inicio = datetime.strptime(data_hora_inicio_str, "%Y-%m-%d %H:%M:%S")
        return now > data_hora_inicio

    def get_horario_disponivel_para_marcar(self, agenda):
        now = datetime.now()
        data_hora_inicio_str = f'{agenda.dia_da_consulta} {agenda.horario_inicial}'
        data_hora_inicio = datetime.strptime(data_hora_inicio_str, "%Y-%m-%d %H:%M:%S")
        return now < data_hora_inicio and (agenda.consulta is None)

    def create(self, validated_data):
        datetime_inicial_str = f"{validated_data['dia_da_consulta']} {validated_data['horario_inicial']}"
        datetime_final_str = f"{validated_data['dia_da_consulta']} {validated_data['horario_final']}"
        datetime_inicial = datetime.strptime(datetime_inicial_str, "%Y-%m-%d %H:%M:%S")
        datetime_final = datetime.strptime(datetime_final_str, "%Y-%m-%d %H:%M:%S")
        if datetime_inicial >= datetime_final:
            raise HorarioInicialMaiorQueFinalException()
        now = datetime.now()
        if datetime_inicial < now or datetime_final < now:
            raise HorarioNoPassadoException()
        agendas_do_dia = Agenda.objects.filter(dia_da_consulta=validated_data['dia_da_consulta'], medico=validated_data['medico'].id)


        for agenda in agendas_do_dia:
            agenda_do_dia_inicial_str = f"{agenda.dia_da_consulta} {agenda.horario_inicial}"
            agenda_do_dia_final_str = f"{agenda.dia_da_consulta} {agenda.horario_final}"
            agenda_do_dia_inicial = datetime.strptime(agenda_do_dia_inicial_str, "%Y-%m-%d %H:%M:%S")
            agenda_do_dia_final = datetime.strptime(agenda_do_dia_final_str, "%Y-%m-%d %H:%M:%S")
            if agenda_do_dia_inicial <= datetime_inicial and datetime_inicial < agenda_do_dia_final:
                raise HorarioOcupadoException()
            if agenda_do_dia_inicial <= datetime_final and datetime_final <= agenda_do_dia_final:
                raise HorarioOcupadoException()

        agenda = Agenda.objects.create(**validated_data, data_hora_inicial=datetime_inicial)
        return agenda



class AgendaListSerializer(serializers.ModelSerializer):
    horario_disponivel_para_marcar = serializers.SerializerMethodField()
    horario_marcado = serializers.SerializerMethodField()
    horario_passou = serializers.SerializerMethodField()
    consulta = ConsultaAgendaSerializer(read_only=True)
    class Meta:
        model = Agenda
        fields = [
            "id",
            'data_hora_inicial',
            "dia_da_consulta",
            "horario_inicial",
            "horario_final",
            "horario_disponivel_para_marcar",
            "horario_marcado",
            'horario_passou',
            "consulta",
            "medico"
        ]
        depth = 1
        extra_kwargs = {
            "id": {"read_only": True},
            "consulta": {"read_only": True},
            "horario_passou": {"read_only": True},
            "data_hora_inicial": {"read_only": True},
        }
    def get_horario_marcado(self, agenda):
        return agenda.consulta is not None

    def get_horario_passou(self, agenda):
        now = datetime.now()
        data_hora_inicio_str = f'{agenda.dia_da_consulta} {agenda.horario_inicial}'
        data_hora_inicio = datetime.strptime(data_hora_inicio_str, "%Y-%m-%d %H:%M:%S")
        return now > data_hora_inicio

    def get_horario_disponivel_para_marcar(self, agenda):
        now = datetime.now()
        data_hora_inicio_str = f'{agenda.dia_da_consulta} {agenda.horario_inicial}'
        data_hora_inicio = datetime.strptime(data_hora_inicio_str, "%Y-%m-%d %H:%M:%S")
        return now < data_hora_inicio and (agenda.consulta is None)