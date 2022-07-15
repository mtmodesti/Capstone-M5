from django.forms import ValidationError
from .models import Convenio
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class RetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = '__all__'
        read_only_fields = ['id']

    def validate_tipo(self, value):
        convenio = Convenio.objects.filter(tipo=value.lower())
        if convenio.count() > 0:
            raise ValidationError("convenio with this tipo already exists.")        
        return value.lower()
    
    def create(self, validated_data):
        return Convenio.objects.create(**validated_data)

