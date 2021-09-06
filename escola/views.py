from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer,CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibir todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer #classe responsavel pelo serializer


class CursoViewset(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


 
"""Registrando URLs"""