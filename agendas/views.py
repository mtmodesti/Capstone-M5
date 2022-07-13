from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Agenda
from .serializers import AgendaSerializer


class ListCreateAgendaView(ListCreateAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer


class RetrieveUpdateDestroyAgendaView(RetrieveUpdateDestroyAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    lookup_url_kwarg = "agenda_id"
