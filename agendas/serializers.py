from rest_framework import serializers

from .models import Agenda


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ["id", "data_consulta", "consulta_id", "medico_id"]

        extra_kwargs = {"id": {"read_only": True}}
