import datetime

from agendas.models import Agenda
from medicos.models import Medico
from medicos.serializers import MedicoSerializer
from pacientes.models import Paciente
from pacientes.serializers import PacienteSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from usuarios.permissions import isSuperUser, isSuperUserOrOwner, isSuperUserOrStaff
from usuarios.serializers import (
    ChangeActivePropertySerializer,
    UsuarioMedicoSerializer,
    UsuarioProfileSerializer,
    UsuarioSerializer,
)

from .models import Usuario


## views para usuários em geral
class ListCreateUsuarioView(generics.ListCreateAPIView):
    permission_classes = [isSuperUser]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class RetrieveUpdateDestroyUsuarioView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperUserOrOwner]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


## Views para agentes de saúde - para super users ou atendentes
class CreateHealthAgentView(generics.CreateAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioMedicoSerializer

    def get_queryset(self):
        return Usuario.objects.filter(agente_de_saude=True)


class ListHealthAgentView(generics.ListAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    def get_queryset(self):

        nome = self.request.query_params.get("nome", None)
        if nome:
            medicos = Medico.objects.all().order_by("nome")
            nomeToLowerCase = nome.lower()
            for medico in Medico.objects.all():
                medicoNameLower = medico.nome.lower()
                if not nomeToLowerCase in medicoNameLower:
                    medicos = medicos.exclude(id=medico.id)

            return medicos

        return super().get_queryset().order_by("nome")


class RetrieveUpdateDeleteHealthAgentView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperUserOrStaff]
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


## Mostra o perfil do usuário
class ShowProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioProfileSerializer

    def get_object(self):
        return self.request.user


## View para tornar o usuário inativo ou ativo
class ChangeActivePropertyView(generics.UpdateAPIView):
    permission_classes = [isSuperUser]
    queryset = Usuario.objects.all()
    serializer_class = ChangeActivePropertySerializer


class ResumoView(APIView):
    def get(self, request):
        pacientes = Paciente.objects.all()
        pacientes_serializer = PacienteSerializer(pacientes, many=True).data
        total_de_inadimplentes = 0
        for paciente in pacientes_serializer:
            if paciente["total_de_consultas"] > paciente["consultas_pagas"]:
                total_de_inadimplentes = total_de_inadimplentes + 1

        total_de_pacientes = Paciente.objects.all().count()
        total_de_medicos = Usuario.objects.filter(agente_de_saude=True).count()
        today = datetime.date.today()
        agendados = Agenda.objects.filter(dia_da_consulta=today)
        for agenda in Agenda.objects.filter(dia_da_consulta=today):
            if agenda.consulta is None:
                agendados = agendados.exclude(id=agenda.id)


        return Response(
            {
                "total_de_pacientes": total_de_pacientes,
                "total_de_medicos": total_de_medicos,
                "total_agendado_hoje": agendados.count(),
                "pacientes_inadimplentes": total_de_inadimplentes,
            }
        )

class ListUpdateAtendente(generics.ListAPIView):
    permission_classes=[isSuperUser]
    queryset = Usuario.objects.filter(is_staff=True, is_superuser=False)
    serializer_class = UsuarioProfileSerializer


class ListAllHealthAgentView(generics.ListAPIView):
    permission_classes = [isSuperUserOrStaff]

    def get(self, request):
        nome = request.query_params.get("nome", None)
        medicos = Medico.objects.all().order_by("nome")

        if nome:
            nomeToLowerCase = nome.lower()
            for medico in Medico.objects.all():
                medicoNameLower = medico.nome.lower()
                if not nomeToLowerCase in medicoNameLower:
                    medicos = medicos.exclude(id=medico.id)

            serializer = MedicoSerializer(medicos, many=True)
            return Response(serializer.data)

        medicos = Medico.objects.all().order_by("nome")
        serializer = MedicoSerializer(medicos, many=True)

        return Response(serializer.data)

