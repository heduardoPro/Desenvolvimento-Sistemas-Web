from django.db import models

# Create your models here.

class Discos(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=False)
    selo_fotografico = models.CharField(max_length=255, blank=True)
    ano = models.DateTimeField(auto_now_add=True)
    pais = models.CharField(max_length=200)
    genero = models.CharField(max_length=255)
    quantidade = models.IntegerField()