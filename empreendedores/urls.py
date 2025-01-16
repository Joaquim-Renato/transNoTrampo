from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_empreendedor, name='cadastrar_empreendedor'),
    path('lista/', views.lista_empreendedores, name='lista_empreendedores'),
    path('', views.index, name='index'),
    path('editar/<int:id>/', views.edit_empreendedor, name='edit_empreendedor'),
    path('deletar/<int:id>/', views.delete_empreendedor, name='delete_empreendedor'),

]
