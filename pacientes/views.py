from typing import Optional
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from convenios.models import Convenio

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
            convenio = self.request.data['convenio']
            convenio, _ = Convenio.objects.get_or_create(id=convenio)
            serializer.save(convenio=convenio)
        else:
            serializer.save()

    def get_queryset(self):
        convenios = self.request.query_params.get("convenio", None)
        if convenios:
            qs = Paciente.objects.all()
            for convenio in convenios.split(self.convenio_separator):
                qs = qs.filter(convenio__tipo=convenio)
            return qs

        nome = self.request.query_params.get("nome", None)
        if nome:
            pacientes = Paciente.objects.all()
            nomeToLowerCase = nome.lower()
            for paciente in Paciente.objects.all():
                pacienteNameLower = paciente.nome.lower()
                if not nomeToLowerCase in pacienteNameLower:
                    pacientes = pacientes.exclude(id=paciente.id)

            return pacientes

        return super().get_queryset()


class RetrieveUpdateDestroyPacienteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperuserOrStaff]

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    lookup_url_kwarg = "paciente_id"
