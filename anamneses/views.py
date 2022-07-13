from rest_framework import generics

from anamneses.serializers import AnamneseSerializer
from .models import Anamnese
# Create your views here.

class ListCreateAnamneseView(generics.ListCreateAPIView):
    queryset = Anamnese.objects.all()
    serializer_class = AnamneseSerializer
    
class RetrieveUpdateDestroyAnamneseView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anamnese.objects.all()
    serializer_class = AnamneseSerializer
