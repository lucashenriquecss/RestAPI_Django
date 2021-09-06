from django.db import models
from django.db.models import fields
from rest_framework import serializers
from escola.models import Aluno,Curso
"""Filtro dos dados"""


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno   
        fields =['id','nome','rg','cpf','data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso   
        fields ='__all__'