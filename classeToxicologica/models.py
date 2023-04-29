from django.db import models

# Create your models here.
class ClasseToxicologica(models.Model):
    nivel_categoria = models.IntegerField()
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nivel_categoria
    
    class Meta:
        verbose_name_plural = "Classes Toxicológicas"