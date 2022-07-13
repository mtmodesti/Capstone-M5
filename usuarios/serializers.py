from asyncore import write
from django.http import Http404, HttpResponse, HttpResponseForbidden
from medicos.serializers import MedicoSerializer
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Usuario
from medicos.models import Medico
import ipdb


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id" ,"nome", "email", "is_active", "password"]
        
        extra_kwargs = {"password": {"write_only": True}}
    
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "nome": instance.nome,
            "email": instance.email,
            "ativo": instance.is_active
        }
    
    def create(self, validated_data):
        return Usuario.objects.criar_usuario(**validated_data)


class MedicoSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    nome = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    especialidade = serializers.CharField(write_only=True)
    telefone = serializers.CharField(write_only=True)
    medico = MedicoSerializer(read_only=True)
    registro_profissional = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exists!.")
        return value

    def create(self, validated_data):
        medico_data = {
            "especialidade": validated_data.pop("especialidade"),
            "registro_profissional": validated_data.pop("registro_profissional"),
            "telefone": validated_data.pop("telefone")
        }
        usuario =  Usuario.objects.criar_agente_de_saude(**validated_data)
        Medico.objects.create(**medico_data, usuario=usuario)
        return usuario
