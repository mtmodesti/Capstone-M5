from .models import Medico
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer





class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

