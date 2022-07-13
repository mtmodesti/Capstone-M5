from convenios.models import Convenio
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Paciente
from .serializers import PacienteSerializer
from .permissions import isSuperUserOrStaff, isSuperUserOrStaffOrOwner


class ListCreatePacienteView(ListCreateAPIView):
    permission_classes = [isSuperUserOrStaff]

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class RetrieveUpdateDestroyPacienteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperUserOrStaffOrOwner]

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    lookup_url_kwarg = "paciente_id"
