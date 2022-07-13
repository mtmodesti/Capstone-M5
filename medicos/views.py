from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import Medico
from .serializers import MedicoSerializer

class ShowDoctorView(ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    

