from rest_framework import serializers
from .models import Anamnese

class AnamneseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anamnese
        fields = "__all__"