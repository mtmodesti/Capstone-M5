from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Paciente
from .permissions import isSuperuserOrStaff
from .serializers import PacienteSerializer


class ListCreatePacienteView(ListCreateAPIView):
    permission_classes = [isSuperuserOrStaff]

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class RetrieveUpdateDestroyPacienteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperuserOrStaff]

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    lookup_url_kwarg = "paciente_id"
