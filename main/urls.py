from django.urls import path
from .views import Index, htmx_cadastrar_cliente
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('salvar-cliente', htmx_cadastrar_cliente, name='salvar-cliente'),
]
