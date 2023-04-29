from django.db import models
from propriedade.models import Propriedade

# Create your models here.
class ProdutorRural(models.Model):
    nome = models.CharField(max_length=255)
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Produtor rural"