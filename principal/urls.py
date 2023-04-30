from django.urls import path
from . import views

urlpatterns = [
    #
    path('', views.DocumentView.as_view(), name='visualizar_documento')
]