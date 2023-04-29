from django.db import models

# Create your models here.

class ResponsaveisTecnicos(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    numero_registro = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Responsáveis técnicos"