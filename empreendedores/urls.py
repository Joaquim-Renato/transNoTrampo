from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("cadastrar/", views.cadastrar_empreendedor, name="cadastrar_empreendedor"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("perfil/<int:empreendedor_id>/", views.perfil_empreendedor, name="perfil_empreendedor"),
    path("empreendedores/", views.lista_empreendedores, name="lista_empreendedores"),
    path("editar/<int:empreendedor_id>/", views.edit_empreendedor, name="edit_empreendedor"),
    path("delete/<int:empreendedor_id>/", views.delete_empreendedor, name="delete_empreendedor"),
    path("sobre/", views.sobre, name="sobre"),
    path("recuperar-senha/", views.recuperar_senha, name="recuperar_senha"),
    path("resetar-senha/<str:token>/", views.resetar_senha, name="resetar_senha"),
    path('social-auth/', include('social_django.urls', namespace='social-auth')),
 
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
