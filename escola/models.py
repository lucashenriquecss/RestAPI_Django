from django.db import models
from datetime import datetime
# Create your models here.
class Aluno(models.Model):
    
    nome = models.CharField(max_length=200)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    
    def __str__(self): #representar o objeto aluno em string
        return self.nome

class Curso(models.Model):
    NIVEL =(
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    ) #variavel de instancia

    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1,choices=NIVEL, blank=False, null=False, default='B')