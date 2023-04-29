from django.contrib import admin
from .models import ResponsaveisTecnicos
# Register your models here.


class ResponsaveisTecnicosAdmin(admin.ModelAdmin):
    list_display = ('id','nome',)
    list_display_links = ('id','nome',)


admin.site.register(ResponsaveisTecnicos, ResponsaveisTecnicosAdmin)