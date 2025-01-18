from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar_empreendedor, name='cadastrar_empreendedor'),
    path('empreendedores/', views.lista_empreendedores, name='lista_empreendedores'),
    path('editar/<int:id>/', views.edit_empreendedor, name='edit_empreendedor'),
    path('delete/<int:id>/', views.delete_empreendedor, name='delete_empreendedor'),
]
