from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import weasyprint
from django.views import View
from .models import *


class DocumentView(View):

    def get(self, request, *args, **kwargs):
        receita_id = request.GET.get('receita_id')
        
        if receita_id:
            try:
                receita = Receita.objects.get(pk=receita_id)
                print(receita)
            except Receita.DoesNotExist:
                return HttpResponse("Receita não encontrada.")
        else:
            return HttpResponse("ID da receita não fornecido.")

        return render(request, 'principal/visualizar_documento.html', {
            'receita': receita
        })

class ReceitaModelPrecautions(View):
    def get(self, request, *args, **kwargs):
        receita_id = request.GET.get('receita_id')
        if receita_id:
            try:
                receita = Receita.objects.get(pk=receita_id)
            except Receita.DoesNotExist:
                return HttpResponse("Receita não encontrada.")
        else:
            return HttpResponse("ID da receita não fornecido.")

        return render(request, 'principal/precautions.html', {
            'receita': receita
        })

class ReceitaModel(View):
    def get(self, request, *args, **kwargs):
        receita_id = request.GET.get('receita_id')
        if receita_id:
            try:
                receita = Receita.objects.get(pk=receita_id)
            except Receita.DoesNotExist:
                return HttpResponse("Receita não encontrada.")
        else:
            return HttpResponse("ID da receita não fornecido.")

        return render(request, 'principal/no-precautions.html', {
            'receita': receita
        })
    
def generate_precautions_pdf(request, id):
    data = {'name': 'receita'}

    receita = Receita.objects.get(pk=id)

    context = {
        'receita': receita,
    }

    template = get_template('principal/precautions.html')
    html = template.render(context)

    pdf = weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
        stylesheets=[weasyprint.CSS(string='body { font-family: serif; }')])

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename=certificate_{}.pdf'.format(data['name'])

    return response


def generate_pdf(request, id):
    data = {'name': 'receita'}

    receita = Receita.objects.get(pk=id)

    context = {
        'receita': receita,
    }

    template = get_template('principal/no-precautions.html')
    html = template.render(context)

    pdf = weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
        stylesheets=[weasyprint.CSS(string='body { font-family: serif; }')])

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename=certificate_{}.pdf'.format(data['name'])

    return response


