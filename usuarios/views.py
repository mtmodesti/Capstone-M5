from rest_framework import generics
from usuarios.permissions import isSuperuserOrCreateOnly


from usuarios.serializers import UsuarioSerializer
from .models import Usuario

class CreateUsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ListUsuariosView(generics.ListAPIView):
    permission_classes = [isSuperuserOrCreateOnly]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    

class RetrieveUpdateDestroyUsuarioView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperuserOrCreateOnly]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer