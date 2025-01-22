from django.urls import path
from .views import cadastrar_empreendedor
from . import views

# rota, view responsável, nome de referência
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar_empreendedor, name='cadastrar_empreendedor'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('perfil/', views.perfil_empreendedor, name='perfil_empreendedor'),
    path('empreendedores/', views.lista_empreendedores, name='lista_empreendedores'),
    path('editar/<int:id>/', views.edit_empreendedor, name='edit_empreendedor'),
    path('delete/<int:id>/', views.delete_empreendedor, name='delete_empreendedor'),
]
