from django.db.models.query import QuerySet
from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer,CursoSerializer, MatriculaSerializer, ListaMatriculasSerializer

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

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasSerializer
"""Registrando URLs"""