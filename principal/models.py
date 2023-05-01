from django.db import models
from django.core.exceptions import ValidationError
from uteis.valida_cnpj import valida_cnpj
from uteis.valida_cpf import valida_cpf





class ResponsaveisTecnicos(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    cnpj = models.CharField(max_length=18, unique=True, help_text='Digite no formato xx.xxx.xxx/xxxx-XX para CNPJ ou xxx.xxx.xxx-xx para CPF.', verbose_name="CPF/CNPJ")
    numero_registro = models.CharField(max_length=255, unique=True, verbose_name="Número de registro")

    def clean(self):

        if not valida_cnpj(self.cnpj) and not valida_cpf(self.cnpj):
            raise ValidationError('CNPJ ou CPF inválido.')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Responsável técnico"

class Propriedade(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    cnpj = models.CharField(max_length=18, unique=True, help_text='Digite no formato xx.xxx.xxx/xxxx-XX para CNPJ.', verbose_name="CNPJ")
    local = models.TextField(verbose_name="Local")
    latitude = models.CharField(max_length=10, verbose_name="Latitude")
    longitude = models.CharField(max_length=10, verbose_name="Longitude")

    def __str__(self):
        return self.descricao

    def clean(self):

        if not valida_cnpj(self.cnpj):
            raise ValidationError('CNPJ inválido.')
    
    class Meta:
        verbose_name_plural = "Propriedade"


class ProdutorRural(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE, verbose_name="Propriedade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Produtor rural"

class ClasseToxicologica(models.Model):
    nivel_categoria = models.IntegerField(unique=True, verbose_name="Nível da categoria")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = "Classes Toxicológicas"

class DiagnosticoRecomendacaoTecnica(models.Model):
    cultura = models.CharField(max_length=255, verbose_name="Cultura")
    produto_comercial = models.CharField(max_length=255, verbose_name="Produto comercial")
    area_a_tratar = models.CharField(max_length=255, verbose_name="Área a tratar")
    volume_da_calda = models.CharField(max_length=255, verbose_name="Volume da calda")
    modalidade_aplicacao = models.CharField(max_length=255, verbose_name="Modalidade de aplicação")
    alvo = models.CharField(max_length=255, verbose_name="Alvo")
    intervalo_de_seguranca = models.CharField(max_length=255, verbose_name="Intervalo de segurança")
    classe_toxicologica = models.ForeignKey(ClasseToxicologica, null=True, on_delete=models.SET_NULL, verbose_name="Classe toxicológica")
    equipamento_aplicacao = models.CharField(max_length=255, verbose_name="Equipamento de aplicação")
    quantidade_a_adquirir = models.CharField(max_length=255, verbose_name="Quantidade a adquirir")
    dosagem = models.CharField(max_length=255, verbose_name="Dosagem")
    numero_aplicacoes = models.IntegerField(verbose_name="Número de aplicações")
    epoca_aplicacao = models.TextField(verbose_name="Época de aplicação")

    class Meta:
        verbose_name_plural = "Diaginósticos e recomendações técnicas"

class Receituario(models.Model):
    responsavel_tecnico = models.ForeignKey(ResponsaveisTecnicos, null=True, on_delete=models.SET_NULL, verbose_name="Responsável técnico")
    produtor_rural = models.ForeignKey(ProdutorRural, null=True, on_delete=models.SET_NULL, verbose_name="Produtor rural")
    diagnosticos_recomendacoes = models.ForeignKey(DiagnosticoRecomendacaoTecnica, null=True, on_delete=models.SET_NULL, verbose_name="Diagnóstico e recomendaçõe técnica")

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name_plural = "Receituário"

