from .models import Medico
from rest_framework import serializers
# from datetime import datetime
from consultas.models import Consulta
from agendas.models import Agenda
import datetime


class MedicoSerializer(serializers.ModelSerializer):
    consultas_a_fazer = serializers.SerializerMethodField()
    consultas_a_fazer_hoje = serializers.SerializerMethodField()
    horarios_livres_agenda = serializers.SerializerMethodField()
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
            'consultas_a_fazer',
            'consultas_a_fazer_hoje',
            'horarios_livres_agenda'
        ]
        extra_kwargs = {
            "agenda": {"read_only": True},
        }
    
    def get_horarios_livres_agenda(self, medico):
        agendas = Agenda.objects.filter(medico=medico.id, consulta=None)
        now = datetime.datetime.now()
        for agenda in Agenda.objects.filter(medico=medico.id):
            dia_c = agenda.dia_da_consulta
            inicial_c = agenda.horario_inicial
            final_c = agenda.horario_final
            datetime_final_str = f"{dia_c} {final_c}"
            datetime_final = datetime.datetime.strptime(datetime_final_str, "%Y-%m-%d %H:%M:%S")
            if now > datetime_final:
               agendas = agendas.exclude(id=agenda.id)
        return agendas.count()


    def get_consultas_a_fazer_hoje(self, medico):
        today = datetime.date.today()
        consultas = Consulta.objects.filter(medico=medico.id)
        for consulta in Consulta.objects.filter(medico=medico.id):
            dia_c = consulta.agenda.dia_da_consulta
            if today > dia_c:
               consultas = consultas.exclude(id=consulta.id)
        return consultas.count()


    def get_consultas_a_fazer(self, medico):
        consultas = Consulta.objects.filter(medico=medico.id)
        now = datetime.datetime.now()
        for consulta in Consulta.objects.filter(medico=medico.id):
            dia_c = consulta.agenda.dia_da_consulta
            final_c = consulta.agenda.horario_final
            datetime_final_str = f"{dia_c} {final_c}"
            datetime_final = datetime.datetime.strptime(datetime_final_str, "%Y-%m-%d %H:%M:%S")
            import ipdb
            if now > datetime_final:
               consultas = consultas.exclude(id=consulta.id)
        return consultas.count()


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

