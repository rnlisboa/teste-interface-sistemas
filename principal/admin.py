from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from .models import *
@admin.register(ClasseToxicologica)
class ClasseToxicologicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nivel_categoria','descricao',)
    list_display_links = ('id', 'nivel_categoria','descricao',)


@admin.register(DiagnosticoRecomendacaoTecnica)
class DiagnosticoRecomendacaoTecnicaAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

@admin.register(ProdutorRural)
class ProdutorRuralAdmin(admin.ModelAdmin):
    list_display = ('id','nome',)
    list_display_links = ('id','nome',)


@admin.register(Propriedade)
class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ('id','descricao',)
    list_display_links = ('id','descricao',)


@admin.register(ResponsaveisTecnicos)
class ResponsaveisTecnicosAdmin(admin.ModelAdmin):
    list_display = ('id','nome',)
    list_display_links = ('id','nome',)


@admin.register(Receituario)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id','responsavel_tecnico','produtor_rural',)
    list_display_links = ('id','responsavel_tecnico','produtor_rural',)
    
    def gerar_receita(self, request, queryset):
        url = reverse('visualizar_documento') + '?' + urlencode({'receita_id': queryset.first()})
        return HttpResponseRedirect(url)

    gerar_receita.short_description = 'Gerar Receituário'

    actions = ['gerar_receita']


