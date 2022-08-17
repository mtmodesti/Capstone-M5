from django.shortcuts import get_object_or_404
from rest_framework import generics
from agendas.models import Agenda
from usuarios.permissions import isSuperUserOrStaff
from django.utils import timezone
from .models import Consulta
from pacientes.models import Paciente
from medicos.models import Medico
from .serializers import ConsultaSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
import ipdb
from datetime import datetime, date
from .exceptions import HorarioMarcadoException, HorarioPassouException, DataInvalidaException


def get_datetime(data):
    dia = data.day
    mes = data.month
    ano = data.year
    hora = data.hour
    minuto = data.minute
    return datetime(ano, mes, dia, hora, minuto, 0)


class ListConsultaView(generics.ListAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    def get_queryset(self):
        data = self.request.query_params.get('data')
        if data:
            consultas = Consulta.objects.all().order_by('horario')
            for consulta in Consulta.objects.all():
                dia = consulta.agenda.dia_da_consulta.day
                mes = consulta.agenda.dia_da_consulta.month
                ano = consulta.agenda.dia_da_consulta.year
                dia_consulta = date(ano, mes, dia)
                data_info_query = data.split('-')
                import pytz
                import ipdb 
                try:
                    dia_query = date(int(data_info_query[2]),int(data_info_query[1]), int(data_info_query[0]))
                except Exception:
                    raise DataInvalidaException()
                
                if dia_query !=dia_consulta:
                    consultas=consultas.exclude(id=consulta.id)
            
            return consultas

        return Consulta.objects.all().order_by('horario')


class CreateConsultaView(generics.CreateAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def perform_create(self, serializer):
        paciente = get_object_or_404(Paciente, pk=self.kwargs["paciente_id"])
        medico = get_object_or_404(Medico, pk=self.kwargs["medico_id"])
        agenda = get_object_or_404(Agenda, pk=self.kwargs['agenda_id'], medico=medico)
        dia = agenda.dia_da_consulta.day
        mes = agenda.dia_da_consulta.month
        ano = agenda.dia_da_consulta.year
        hora = agenda.horario_inicial.hour
        minuto = agenda.horario_inicial.minute
        data_hora_inicial = datetime(ano, mes, dia, hora, minuto, 0)
        now = datetime.now()
        if data_hora_inicial < now:
            raise HorarioPassouException()

        if agenda.__dict__['consulta_id'] is not None:
            raise HorarioMarcadoException()

        send_mail(
            subject=f"Consulta - Doutor(a) {medico.nome}",
            message=f"Olá, {paciente.nome}!\n\nEste é um e-mail de confirmação para a sua consulta que está agendada para o dia {agenda.data_hora_inicial.strftime('%d/%m/%Y às %H:%M')}.\n\nCaso não seja possível comparecer, por favor, nos avise com o máximo de antecedência!\n\nAtenciosamente, Clinika",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[f"{paciente.email}"],
            fail_silently=False,
        )

        return serializer.save(
            usuario=self.request.user,
            paciente=self.kwargs["paciente_id"],
            medico=self.kwargs["medico_id"],
            horario_agenda=self.kwargs['agenda_id']
        )


class FiltrarConsultaMedicoView(generics.ListAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        return Consulta.objects.filter(medico=self.kwargs["medico_id"]).order_by('horario')


class RetrieveUpdateDestroyConsultaView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


class FiltrarConsultaPacienteView(generics.ListAPIView):
    parser_classes = [isSuperUserOrStaff]
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    def get_queryset(self):
        data = self.request.query_params.get('data')
        if data:
            consultas = Consulta.objects.all().order_by('horario')
            for consulta in Consulta.objects.all():
                dia = consulta.agenda.dia_da_consulta.day
                mes = consulta.agenda.dia_da_consulta.month
                ano = consulta.agenda.dia_da_consulta.year
                dia_consulta = date(ano, mes, dia)
                data_info_query = data.split('-')
                try:
                    dia_query = date(int(data_info_query[2]),int(data_info_query[1]), int(data_info_query[0]))
                except Exception:
                    raise DataInvalidaException()

                if dia_query !=dia_consulta:
                    consultas=consultas.exclude(id=consulta.id)

            return consultas

        return Consulta.objects.filter(paciente=self.kwargs["paciente_id"]).order_by('horario')