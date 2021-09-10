from django.db.models.query import QuerySet
from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer,CursoSerializer, MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibir todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer #classe responsavel pelo serializer


class CursoViewset(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewset(viewsets.ModelViewSet):
     QuerySet = Matricula.objects.all()
     serializer_class = MatriculaSerializer

"""Registrando URLs"""