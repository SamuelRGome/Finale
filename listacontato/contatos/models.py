from django.db import models

# Create your models here.
class Contato(models.Model):
    nome_completo = models.CharField(max_length=500)
    relacao = models.CharField(max_lenght=50)
    email = models.EmailField(max_length=254)
    numero = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome_completo
