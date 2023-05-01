from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import itertools
from django.views import View
from .models import *

import pdfkit
config = pdfkit.configuration(wkhtmltopdf=r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

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
    
def generate_precautions_pdf(request, receita_id):
    receita_id = receita_id
    if receita_id:
        url = request.build_absolute_uri(reverse('precautions')) + "?receita_id=" + str(receita_id)
        pdf = pdfkit.from_url(url,configuration=config)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="receita_mod.pdf"'
        return response
    else:
        return HttpResponse("ID da receita não fornecido.")


def generate_pdf(request, receita_id):
    receita_id = receita_id
    if receita_id:
        url = request.build_absolute_uri(reverse('no-precautions')) + "?receita_id=" + str(receita_id)
        pdf = pdfkit.from_url(url,configuration=config)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="receita_mod.pdf"'
        return response
    else:
        return HttpResponse("ID da receita não fornecido.")
