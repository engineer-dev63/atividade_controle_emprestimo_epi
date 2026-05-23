from django.db import models

# Create your models here.
from django.db import models

class Colaborador(models.Model):
    # Aqui definimos os campos que vão virar colunas no banco de dados
    nome = models.CharField(max_length=150)
    cargo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50, unique=True) # unique=True impede matrículas duplicadas

    def __str__(self):
        return self.nome