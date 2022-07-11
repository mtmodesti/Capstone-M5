from .models import Convenio
from rest_framework import serializers

class ConvenioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    
    ...