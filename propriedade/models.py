from django.db import models

# Create your models here.

class Propriedade(models.Model):
    descricao = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    local = models.TextField()
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = "Propriedade"