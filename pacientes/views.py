from convenios.models import Convenio
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Paciente
from .serializers import PacienteSerializer


class ListCreatePacienteView(ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class RetrieveUpdateDestroyPacienteView(RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    lookup_url_kwarg = "paciente_id"
