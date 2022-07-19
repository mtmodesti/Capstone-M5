from pacientes.models import Paciente
from rest_framework import generics
from rest_framework.reverse import reverse
from usuarios.permissions import isSuperUserOrStaff
from django.utils import timezone
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

class FiltrarConsultaMedicoView(generics.ListAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    def get_queryset(self):
        return Consulta.objects.filter(medico=self.kwargs['medico_id'])


class RetrieveUpdateDestroyConsultaView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


class FiltrarConsultasMaisProximasDeAcontecerView(generics.ListAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    def get_queryset(self):
        now = timezone.now()
        queries = Consulta.objects.all()
        for query in queries:
            if query.data_da_consulta < now:
                queries = queries.exclude(id=query.id)

        return queries.order_by('data_da_consulta')


class FiltrarConsultasMaisProximasDeAcontecerPorMedicoView(generics.ListAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    def get_queryset(self):
        now = timezone.now()
        queries = Consulta.objects.filter(medico=self.kwargs['medico_id'])
        for query in queries:
            if query.data_da_consulta < now:
                queries = queries.exclude(id=query.id)

        return queries.order_by('data_da_consulta')

