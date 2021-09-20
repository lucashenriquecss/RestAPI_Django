from django.db.models.query import QuerySet
from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer,CursoSerializer, MatriculaSerializer, ListaMatriculasSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentocation
from rest_framework.permissions  import IsAuthenticated
class AlunosViewSet(viewsets.ModelViewSet):
    """Exibir todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer #classe responsavel pelo serializer
    authentication_classes = [BasicAuthentocation]
    permission_classes = [ IsAuthenticated]

class CursoViewset(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentocation]
    permission_classes = [ IsAuthenticated]

class MatriculaViewset(viewsets.ModelViewSet):
    QuerySet = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentocation]
    permission_classes = [ IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasSerializer
    authentication_classes = [BasicAuthentocation]
    permission_classes = [ IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentocation]
    permission_classes = [ IsAuthenticated]

"""Registrando URLs"""