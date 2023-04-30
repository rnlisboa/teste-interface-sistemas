from django.db import models

# Create your models here.
class ResponsaveisTecnicos(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    numero_registro = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Responsável técnico"

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


class ProdutorRural(models.Model):
    nome = models.CharField(max_length=255)
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Produtor rural"

class ClasseToxicologica(models.Model):
    nivel_categoria = models.IntegerField()
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = "Classes Toxicológicas"

class DiagnosticoRecomendacaoTecnica(models.Model):
    cultura = models.CharField(max_length=255)
    produto_comercial = models.CharField(max_length=255)
    area_a_tratar = models.CharField(max_length=255)
    volume_da_calda = models.CharField(max_length=255)
    modalidade_aplicacao = models.CharField(max_length=255)
    alvo = models.CharField(max_length=255)
    intervalo_de_seguranca = models.CharField(max_length=255)
    classe_toxicologica = models.ForeignKey(ClasseToxicologica, null=True, on_delete=models.SET_NULL)
    equipamento_aplicacao = models.CharField(max_length=255)
    quantidade_a_adquirir = models.CharField(max_length=255)
    dosagem = models.CharField(max_length=255)
    numero_aplicacoes = models.IntegerField()
    epoca_aplicacao = models.TextField()

    class Meta:
        verbose_name_plural = "Diaginósticos e recomendações técnicas"

class Receita(models.Model):
    responsavel_tecnico = models.ForeignKey(ResponsaveisTecnicos, null=True, on_delete=models.SET_NULL)
    produtor_rural = models.ForeignKey(ProdutorRural, null=True, on_delete=models.SET_NULL)
    diagnosticos_recomendacoes = models.ForeignKey(DiagnosticoRecomendacaoTecnica, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.id}"



