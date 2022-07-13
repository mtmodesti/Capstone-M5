from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Agenda
from .permissions import isSuperUserOrStaffOrOwner
from .serializers import AgendaSerializer


class ListCreateAgendaView(ListCreateAPIView):
    pagination_class = [isSuperUserOrStaffOrOwner]

    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer


class RetrieveUpdateDestroyAgendaView(RetrieveUpdateDestroyAPIView):
    pagination_class = [isSuperUserOrStaffOrOwner]

    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    lookup_url_kwarg = "agenda_id"
