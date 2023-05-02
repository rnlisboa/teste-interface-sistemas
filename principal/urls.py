from django.urls import path
from . import views

urlpatterns = [
    path('', views.DocumentView.as_view(), name='visualizar_documento'),
    path('pdf/<int:id>', views.generate_precautions_pdf, name='precautions'),
    path('pdf-2/<int:id>', views.generate_pdf, name='no-precautions')
]