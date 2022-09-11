from urllib import request
from django.shortcuts import get_object_or_404
from rest_framework import generics
from medicos.models import Medico
from .models import Agenda
from .permissions import isSuperUserOrStaffOrOwner
from .serializers import AgendaSerializer, AgendaListSerializer
import datetime
from .exceptions import DataInválidaException


class ListarAgendaView(generics.ListAPIView):
    queryset = Agenda.objects.all()
    permission_classes = [isSuperUserOrStaffOrOwner]
    serializer_class = AgendaListSerializer
    def get_queryset(self):
        agendas = Agenda.objects.all()
        data = self.request.query_params.get('data')
        if data:
            data_separada = data.split('-')
            try:
                date = datetime.date(int(data_separada[2]), int(data_separada[1]), int(data_separada[0]) )
            except Exception:             
                raise DataInválidaException()
            agendas = agendas.filter(dia_da_consulta=date)
            return agendas.order_by('data_hora_inicial')

        return agendas.order_by('data_hora_inicial')


class ListCreateAgendaView(generics.ListCreateAPIView):
    permission_classes = [isSuperUserOrStaffOrOwner]
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    def get_queryset(self):
        data = self.request.query_params.get('data')
        agendas = Agenda.objects.all()
        agendas = agendas.filter(medico=self.kwargs['medico_id'])
        if data:
            data_separada = data.split('-')
            try:
                date = datetime.date(int(data_separada[2]), int(data_separada[1]), int(data_separada[0]) )
            except Exception:             
                raise DataInválidaException()
            agendas = agendas.filter(dia_da_consulta=date)
            return agendas.order_by('data_hora_inicial')

        return agendas.order_by('data_hora_inicial')

    def perform_create(self, serializer):
        medico = get_object_or_404(Medico, pk=self.kwargs['medico_id'])
        serializer.save(medico=medico)


class RetrieveUpdateDestroyAgendaView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperUserOrStaffOrOwner]
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    lookup_url_kwarg = "agenda_id"




class ListarHorariosVagosMedicosView(generics.ListAPIView):
    permission_classes = [isSuperUserOrStaffOrOwner]
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    def get_queryset(self):
        data = self.request.query_params.get('data')
        agendas = Agenda.objects.filter(medico=self.kwargs['medico_id'], consulta=None)
        if data:
            data_separada = data.split('-')
            try:
                date = datetime.date(int(data_separada[2]), int(data_separada[1]), int(data_separada[0]) )
            except Exception:             
                raise DataInválidaException()
            agendas = agendas.filter(dia_da_consulta=date)
            return agendas.order_by('data_hora_inicial')

        return agendas.order_by('data_hora_inicial')

