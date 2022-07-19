from django.shortcuts import get_object_or_404
from rest_framework import generics
from usuarios.permissions import isSuperUserOrStaff
from django.utils import timezone
from .models import Consulta
from pacientes.models import Paciente
from medicos.models import Medico
from .serializers import ConsultaSerializer
from django.core.mail import send_mail
from django.conf import settings
import ipdb


class ListConsultaView(generics.ListAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


class CreateConsultaView(generics.CreateAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def perform_create(self, serializer):
        paciente = get_object_or_404(Paciente, pk=self.kwargs["paciente_id"])
        medico = get_object_or_404(Medico, pk=self.kwargs["medico_id"])
        # paciente = Paciente.objects.get(pk=self.kwargs["paciente_id"])
        # medico = Medico.objects.get(pk=self.kwargs["medico_id"])
        send_mail(
            subject=f"Consulta - Doutor(a) {medico.nome}",
            message=f"Olá, {paciente.nome}!\n\nEste é um e-mail de confirmação para a sua consulta que está agendada para o dia {serializer.validated_data['data_da_consulta'].strftime('%d/%m/%Y às %H:%M')}.\n\nCaso não seja possível comparecer, por favor, nos avise com o máximo de antecedência!\n\nAtenciosamente, Clinika",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[f"{paciente.email}"],
            fail_silently=False,
        )

        return serializer.save(
            usuario=self.request.user,
            paciente=self.kwargs["paciente_id"],
            medico=self.kwargs["medico_id"],
        )


class FiltrarConsultaMedicoView(generics.ListAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        return Consulta.objects.filter(medico=self.kwargs["medico_id"])


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

        return queries.order_by("data_da_consulta")


class FiltrarConsultasMaisProximasDeAcontecerPorMedicoView(generics.ListAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        now = timezone.now()
        queries = Consulta.objects.filter(medico=self.kwargs["medico_id"])
        for query in queries:
            if query.data_da_consulta < now:
                queries = queries.exclude(id=query.id)

        return queries.order_by("data_da_consulta")
