
from django.contrib import admin
from django.urls import path
from escola.views import alunos #importando função aluno
urlpatterns = [
    path('alunos/',alunos),
    path('admin/', admin.site.urls),
]
