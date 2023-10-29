from django.db import models

# Create your models here.

from django.db import models


class SeloFonografico(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    discos = models.ManyToManyField('Disco')

    def __str__(self) -> str:
        return self.nome

class Disco(models.Model):
    titulo = models.CharField(max_length=255, blank=True)
    descricao = models.TextField()
    selo_fonografico = models.ForeignKey(SeloFonografico, on_delete=models.CASCADE)
    ano = models.DateTimeField(auto_now_add=True)
    pais = models.CharField(max_length=200)
    genero = models.CharField(max_length=255)
    quantidade = models.IntegerField()

    def __str__(self) -> str:
        return self.titulo