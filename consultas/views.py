from pacientes.models import Paciente
from rest_framework import generics
from rest_framework.reverse import reverse

from .models import Consulta
from .serializers import ConsultaSerializer

Paciente


class ListCreateConsultaView(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


    def perform_create(self, serializer):
      

        return serializer.save(usuario=self.request.user, paciente=self.kwargs["paciente_id"])

class RetrieveUpdateDestroyConsultaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
