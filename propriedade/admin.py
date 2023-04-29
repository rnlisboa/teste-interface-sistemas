from django.contrib import admin
from .models import Propriedade
# Register your models here.


class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ('id','descricao',)
    list_display_links = ('id','descricao',)


admin.site.register(Propriedade, PropriedadeAdmin)
