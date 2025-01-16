from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_empreendedor, name='cadastrar_empreendedor'),
    path('lista/', views.lista_empreendedores, name='lista_empreendedores'),
    path('', views.index, name='index')
]
