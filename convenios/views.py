from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    UpdateAPIView,
)
from .models import Convenio
from pacientes.models import Paciente
from .serializers import RetrieveUpdateDestroySerializer
from .mixins import SerializeByMethodMixin
from convenios.permissions import isSuperUser
from usuarios.permissions import isSuperUserOrStaff


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    permission_classes = [isSuperUser]

    queryset = Convenio.objects.all()

    serializer_class = RetrieveUpdateDestroySerializer


class CreateConvenioView(ListCreateAPIView):

    permission_classes = [isSuperUser]

    queryset = Convenio.objects.all()

    serializer_class = RetrieveUpdateDestroySerializer


class AssociateConvenioWithPatientView(UpdateAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Convenio.objects.all()
    serializer_class = RetrieveUpdateDestroySerializer

    def perform_update(self, serializer):
        paciente = get_object_or_404(Paciente, pk=self.kwargs["paciente_id"])
        convenio = get_object_or_404(Convenio, pk=self.kwargs["pk"])
        paciente.convenio = convenio
        paciente.save()
        serializer.save()
