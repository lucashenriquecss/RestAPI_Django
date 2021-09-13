from django.db import models
from django.db.models import fields
from rest_framework import serializers
from escola.models import Aluno,Curso, Matricula
"""Filtro dos dados"""


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno   
        fields =['id','nome','rg','cpf','data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso   
        fields ='__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude =[]


class ListaMatriculasSerializer(serializers.ModelSerializer): # Responsavel por listar todas as matriculas
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']