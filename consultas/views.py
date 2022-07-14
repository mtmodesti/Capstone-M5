from pacientes.models import Paciente
from rest_framework import generics
from rest_framework.reverse import reverse

from usuarios.permissions import isSuperUserOrStaff

from .models import Consulta
from .serializers import ConsultaSerializer


class ListConsultaView(generics.ListAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


class CreateConsultaView(generics.CreateAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def perform_create(self, serializer):
        return serializer.save(
            usuario=self.request.user,
            paciente=self.kwargs["paciente_id"],
            medico=self.kwargs["medico_id"]
        )

class RetrieveUpdateDestroyConsultaView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
