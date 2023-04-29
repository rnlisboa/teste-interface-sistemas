from django.contrib import admin
from .models import DiagnosticoRecomendacaoTecnica
# Register your models here.


class DiagnosticoRecomendacaoTecnicaAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)


admin.site.register(DiagnosticoRecomendacaoTecnica, DiagnosticoRecomendacaoTecnicaAdmin)
