from .models import Convenio
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Convenio


class ConvenioSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Convenio
        fields = '__all__'
    