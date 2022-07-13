from .models import Medico
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from agendas.models import Agenda
from agendas.serializers import AgendaSerializer


class MedicoSerializer(serializers.ModelSerializer):

    agenda = AgendaSerializer(read_only=True)

    class Meta:
        model = Medico
        fields = '__all__'

    def create(self, validated_data):
    #    import ipdb
 #       import uuid
#        teste = uuid.uuid1()
  #      print(teste)
   #     agenda = Agenda(data_consulta = '-00-00', medico_id=teste)
        Agenda.objects.create()
        
        return Medico.objects.create(**validated_data)
        

