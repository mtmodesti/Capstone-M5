from typing import Optional
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Paciente
from .permissions import isSuperuserOrStaff
from .serializers import PacienteSerializer


class ListCreatePacienteView(ListCreateAPIView):
    permission_classes = [isSuperuserOrStaff]

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    convenio_separator = ","

    def get_queryset(self):
        convenios = self.request.query_params.get("convenio", None)
        if convenios:
            qs = Paciente.objects.all()
            for convenio in convenios.split(self.convenio_separator):
                qs = qs.filter(convenio__tipo=convenio)
            return qs

        return super().get_queryset()


class RetrieveUpdateDestroyPacienteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperuserOrStaff]

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    lookup_url_kwarg = "paciente_id"
