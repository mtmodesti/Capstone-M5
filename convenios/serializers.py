from .models import Convenio
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class RetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Convenio
        fields = '__all__'
        read_only_fields = ['id']

    def validate_tipo(self, value):
        return value.lower()
        
    def create(self, validated_data):
        return Convenio.objects.create(**validated_data)


