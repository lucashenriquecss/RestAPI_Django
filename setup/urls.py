
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet,CursoViewset, MatriculaViewset
from rest_framework import routers

router = routers.DefaultRouter() #rota principal default
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursoViewset, basename='Cursos')
router.register('matricula', MatriculaViewset, basename='Matriculas')

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
