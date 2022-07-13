from rest_framework import generics
from usuarios.permissions import isSuperUser
from usuarios.serializers import UsuarioSerializer, MedicoSerializer
from .models import Usuario


class ListCreateUsuarioView(generics.ListCreateAPIView):
    permission_classes = [isSuperUser]
    queryset = Usuario.objects.all()
    
    serializer_class = UsuarioSerializer

class RetrieveUpdateDestroyUsuarioView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperUser]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ListCreateHealthAgentView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = MedicoSerializer
