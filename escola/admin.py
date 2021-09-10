from django.contrib import admin
from escola.models import Aluno, Curso, Matricula
# Register your models here.
"""Configurar o admin para criar e atualizar os alunos e cursos """


class Alunos(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'rg',
        'cpf',
        'data_nascimento'
    )
    list_display_links = ('id','nome')#serve para interações para clicar

    search_fields=('nome','cpf','rg') #Campo de busca por nome,cpf ou rg
    list_per_page = 20 #paginação , 20 alunos por pagina

admin.site.register(Aluno,Alunos)



class Cursos(admin.ModelAdmin):
    list_display =(
        'id',
        'codigo_curso',
        'descricao',
        'nivel'
    )
    list_display_links=('id', 'codigo_curso')
    search_fields=('codigo_curso', 'nivel')
    
admin.site.register(Curso,Cursos)




class Matriculas(admin.ModelAdmin):
    list_display =(
        'id',
        'aluno',
        'curso',
        'periodo',
    )
    list_display_links=('id',)
    
    
admin.site.register(Matricula,Matriculas)