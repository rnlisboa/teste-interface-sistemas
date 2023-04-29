from django.db import models
from classeToxicologica.models import ClasseToxicologica
# Create your models here.
class DiagnosticoRecomendacaoTecnica(models.Model):
    cultura = models.CharField(max_length=255)
    produto_comercial = models.CharField(max_length=255)
    area_a_tratar = models.CharField(max_length=255)
    volume_da_calda = models.CharField(max_length=255)
    modalidade_aplicacao = models.CharField(max_length=255)
    alvo = models.CharField(max_length=255)
    intervalo_de_seguranca = models.CharField(max_length=255)
    classe_toxicologica = models.ForeignKey(ClasseToxicologica, null=True,on_delete=models.SET_NULL)
    equipamento_aplicacao = models.CharField(max_length=255)
    quantidade_a_adquirir = models.IntegerField()
    numero_aplicacoes = models.IntegerField()
    epoca_aplicacao = models.TextField()

    class Meta:
        verbose_name_plural = "Diaginósticos e recomendações técnicas"