from django.shortcuts import get_object_or_404
from rest_framework import generics

from anamneses.serializers import AnamneseSerializer
from pacientes.models import Paciente
from .models import Anamnese
from usuarios.permissions import isSuperUserOrStaff, isSuperUser
# Create your views here.

class ListAnamneseView(generics.ListAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Anamnese.objects.all()
    serializer_class = AnamneseSerializer


class CreateAnamneseView(generics.CreateAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Anamnese.objects.all()
    serializer_class = AnamneseSerializer
    def perform_create(self, serializer):
        paciente = get_object_or_404(Paciente, pk=self.kwargs['paciente_id'])
        serializer.save(paciente=paciente)


class RetrieveUpdateDestroyAnamneseView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Anamnese.objects.all()
    serializer_class = AnamneseSerializer
