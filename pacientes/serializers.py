from pyexpat import model
from django.forms import ValidationError
from django.utils import timezone
from rest_framework import serializers
from convenios.serializers import RetrieveUpdateDestroySerializer
from .models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    # convenio = RetrieveUpdateDestroySerializer()
    total_de_consultas = serializers.SerializerMethodField()
    consultas_pagas = serializers.SerializerMethodField()
    class Meta:
        model = Paciente
        fields = [
            "id",
            "nome",
            "email",
            "cpf",
            "status",
            "telefone",
            "data_nascimento",
            "convenio",
            "anamnese",
            "total_de_consultas",
            "consultas_pagas",
            "data_cadastro",
            "atualizado_em",
        ]
        depth = 1
        read_only_fields = ["id", "data_cadastro", "atualizado_em", 'anamnese']

    def get_total_de_consultas(self, paciente):
        return paciente.consulta.count()

    def get_consultas_pagas(self, paciente):
        return paciente.consulta.filter(pago=True).count()

    def create(self, validated_data):
        now = timezone.now()
        return Paciente.objects.create(**validated_data, data_cadastro=now)
    
    def validate_cpf(self, value):
        if len(value) != 14:
            raise ValidationError("Cpf precisa ter 11 caracteres")
        return value


class PacienteConsultaSerializer(serializers.ModelSerializer):
    # convenio = RetrieveUpdateDestroySerializer(read_only=True)
    class Meta:
        model = Paciente
        fields = [
            "id",
            "nome",
            "email",
            "cpf",
            "status",
            "telefone",
            "data_nascimento",
            "convenio",
            "data_cadastro",
            "atualizado_em",
        ]
        depth = 1
        read_only_fields = ["id", "data_cadastro", "atualizado_em"]


class PacienteAnamneseSerializer(serializers.ModelSerializer):
     class Meta:
        model = Paciente
        fields = [
            "id",
            "nome",
            "email",
            "status",
            "cpf",
            "telefone"
        ]