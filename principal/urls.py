from django.urls import path
from . import views

urlpatterns = [
    path('', views.DocumentView.as_view(), name='visualizar_documento'),
    path('precautions/', views.ReceitaModelPrecautions.as_view(), name='precautions'),
    path('no-precautions/', views.ReceitaModel.as_view(), name='no-precautions'),
    path('pdf/<int:receita_id>', views.generate_precautions_pdf, name='precautions'),
    path('pdf-2/<int:receita_id>', views.generate_pdf, name='no-precautions')
]