from django.contrib import admin
from .models import ClasseToxicologica
# Register your models here.


class ClasseToxicologicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nivel_categoria','descricao',)
    list_display_links = ('id', 'nivel_categoria','descricao',)


admin.site.register(ClasseToxicologica, ClasseToxicologicaAdmin)