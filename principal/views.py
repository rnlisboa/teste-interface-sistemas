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
            except Receita.DoesNotExist:
                return HttpResponse("Receita não encontrada.")
        else:
            return HttpResponse("ID da receita não fornecido.")

        return render(request, 'principal/visualizar_documento.html', {
            'receita': receita
        })
    
def generate_pdf(request):
    receita_id = request.GET.get('receita_id')
    if receita_id:
        url = request.build_absolute_uri(reverse('visualizar_documento')) + "?receita_id=" + receita_id
        print(url)
        pdf = pdfkit.from_url(url,configuration=config)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="receita_mod.pdf"'
        return response
    else:
        return HttpResponse("ID da receita não fornecido.")
