from django.contrib import admin
from .models import ProdutorRural
# Register your models here.


class ProdutorRuralAdmin(admin.ModelAdmin):
    list_display = ('id','nome',)
    list_display_links = ('id','nome',)


admin.site.register(ProdutorRural, ProdutorRuralAdmin)
