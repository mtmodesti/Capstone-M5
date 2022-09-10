from typing import Optional

from convenios.models import Convenio
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from .models import Paciente
from .permissions import isSuperuserOrStaff
from .serializers import PacienteSerializer


class ListCreatePacienteView(ListCreateAPIView):
    permission_classes = [isSuperuserOrStaff]

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    convenio_separator = ","

    def perform_create(self, serializer):
        if "convenio" in self.request.data:
            convenio = self.request.data["convenio"]
            convenio, _ = Convenio.objects.get_or_create(id=convenio)
            serializer.save(convenio=convenio)
        else:
            serializer.save()

    def get_queryset(self):
        convenios = self.request.query_params.get("convenio", None)
        if convenios:
            qs = Paciente.objects.all().order_by("nome")
            for convenio in convenios.split(self.convenio_separator):
                qs = qs.filter(convenio__tipo=convenio)
            return qs

        nome = self.request.query_params.get("nome", None)
        if nome:
            pacientes = Paciente.objects.all().order_by("nome")
            nomeToLowerCase = nome.lower()
            for paciente in Paciente.objects.all():
                pacienteNameLower = paciente.nome.lower()
                if not nomeToLowerCase in pacienteNameLower:
                    pacientes = pacientes.exclude(id=paciente.id)

            return pacientes

        return super().get_queryset().order_by("nome")


class RetrieveUpdateDestroyPacienteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperuserOrStaff]

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    lookup_url_kwarg = "paciente_id"


class ListAllPacientesView(ListAPIView):
    permission_classes = [isSuperuserOrStaff]

    def get(self, request):
        medicos = Paciente.objects.all().order_by("nome")
        serializer = PacienteSerializer(medicos, many=True)

        return Response(serializer.data)
