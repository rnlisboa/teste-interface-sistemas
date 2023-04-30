from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class DocumentView(View):
    def get(self, request, *args, **kwargs):
        receita_id = self.request.GET.get('receita_id')
        receita = Receita.objects.get(pk=receita_id)

        return render(request, 'principal/visualizar_documento.html', {
            'receita': receita
        })