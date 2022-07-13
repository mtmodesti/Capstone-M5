from rest_framework import generics
from usuarios.permissions import isSuperUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from usuarios.serializers import UsuarioSerializer, MedicoSerializer
from .models import Usuario
from rest_framework_simplejwt.authentication import JWTAuthentication
import ipdb

class ListCreateUsuarioView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, isSuperUser]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RetrieveUpdateDestroyUsuarioView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, isSuperUser]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ListCreateHealthAgentView(generics.ListCreateAPIView):
    permission_classes = [isSuperUser]
    queryset = Usuario.objects.all()
    serializer_class = MedicoSerializer

    def get_queryset(self):
        return Usuario.objects.filter(agente_de_saude=True)

class RetrieveUpdateDeleteHealthAgentView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperUser]
    queryset = Usuario.objects.all()
    serializer_class = MedicoSerializer

    def get_queryset(self):
        return Usuario.objects.filter(agente_de_saude=True)
