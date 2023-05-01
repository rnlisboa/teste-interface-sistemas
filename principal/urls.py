from django.urls import path
from . import views

urlpatterns = [
    path('', views.DocumentView.as_view(), name='visualizar_documento'),
    path('pdf/', views.generate_pdf, name='pdf')
]