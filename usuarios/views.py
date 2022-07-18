from rest_framework import generics
from medicos.models import Medico
from usuarios.permissions import isSuperUser, isSuperUserOrStaff, isSuperUserOrOwner
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from usuarios.serializers import (
    ChangeActivePropertySerializer,
    UsuarioSerializer,
    UsuarioMedicoSerializer,
    UsuarioProfileSerializer,
)
from .models import Usuario
from rest_framework_simplejwt.authentication import JWTAuthentication
from medicos.serializers import MedicoSerializer


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
