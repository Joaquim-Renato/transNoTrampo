from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Empreendedor
from .forms import EmpreendedorForm
from .formsedit import EmpreendedorEdicaoForm  # Formulário de edição
from .utils import criptografia, verificar_senha
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.conf import settings



def cadastrar_empreendedor(request):
    if request.method == "POST":
        formulario = EmpreendedorForm(request.POST)
        if formulario.is_valid():
            empreendedor = formulario.save(commit=False)
            senha = formulario.cleaned_data.get("senha")
            empreendedor.senha = criptografia(senha)  # Criptografa a senha
            empreendedor.save()
            messages.success(request, "Empreendedor cadastrado com sucesso!")
            return redirect("login")
        else:
            messages.error(request, "Erro ao cadastrar. Verifique os dados.")
    else:
        formulario = EmpreendedorForm()
    return render(request, "cadastrar.html", {"form": formulario})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        if not email or not senha:
            messages.error(request, "Preencha todos os campos.")
            return render(request, "login.html")

        try:
            empreendedor = Empreendedor.objects.get(email=email)
            if verificar_senha(senha, empreendedor.senha):
                 # Armazena o ID do empreendedor na sessão
                request.session["empreendedor_id"] = empreendedor.id
                messages.success(request, "Login realizado com sucesso!")

                return redirect("perfil_empreendedor", empreendedor_id=empreendedor.id)
            else:
                messages.error(request, "Senha incorreta.")
        except Empreendedor.DoesNotExist:
            messages.error(request, "E-mail não encontrado.")
    return render(request, "login.html")


def logout_view(request):
    if "empreendedor_id" in request.session:
        del request.session["empreendedor_id"]
    messages.success(request, "Logout realizado com sucesso.")
    return redirect("login")



def perfil_empreendedor(request, empreendedor_id):
    empreendedor = get_object_or_404(Empreendedor, id=empreendedor_id)
    return render(request, "perfil.html", {"empreendedor": empreendedor})



def edit_empreendedor(request, empreendedor_id):
    empreendedor = get_object_or_404(Empreendedor, id=empreendedor_id)
   
    if request.method == "POST":
        formulario = EmpreendedorEdicaoForm(request.POST, request.FILES, instance=empreendedor)
        
        if formulario.is_valid():

            senha = formulario.cleaned_data.get("senha")
            if senha:
                empreendedor.senha = criptografia(senha)

            formulario.save()

            messages.success(request, "Dados atualizados com sucesso!")
            next_url = request.GET.get('next', 'perfil_empreendedor')
            return redirect(next_url, empreendedor_id=empreendedor.id)
        else:
            messages.error(request, "Erro ao atualizar os dados.")
    else:
        formulario = EmpreendedorEdicaoForm(instance=empreendedor)
    
    return render(request, 'editar.html', {'form': formulario, 'empreendedor': empreendedor})


def delete_empreendedor(request, empreendedor_id):
    empreendedor = get_object_or_404(Empreendedor, id=empreendedor_id)
   
    if request.method == "POST":
        empreendedor.delete()
        messages.success(request, "Empreendedor excluído com sucesso!")
        return redirect("lista_empreendedores")
    return render(request, "delete.html", {"empreendedor": empreendedor})


def lista_empreendedores(request):
    query = request.GET.get('q')  # Captura o termo da pesquisa
    if query:
        empreendedores = Empreendedor.objects.filter(
            nome__icontains=query
        ) | Empreendedor.objects.filter(
            servico__icontains=query
        )
    else:
    
        empreendedores = Empreendedor.objects.all()
    return render(request, "lista.html", {"empreendedores": empreendedores})


def index(request):
    return render(request, "index.html")


def sobre(request):
    return render(request, "sobre.html")

# Dicionário temporário para armazenar tokens (melhor usar um modelo ou cache)
reset_tokens = {}


def recuperar_senha(request):
    """ Envia um e-mail com link para redefinir senha """
    if request.method == "POST":
        email = request.POST.get("email")

        try:
            empreendedor = Empreendedor.objects.get(email=email)
            token = get_random_string(50)  # Gera um token aleatório
            reset_tokens[token] = empreendedor.email  # Armazena o token temporariamente

            reset_link = f"{request.build_absolute_uri('/resetar-senha/')}{token}/"
            send_mail(
                "Recuperação de Senha", # Assunto do e-mail
                f"Olá, clique no link para redefinir sua senha: {reset_link}",  # Corpo do e-mail
                settings.DEFAULT_FROM_EMAIL, # Remetente (configurado nas settings do Django)
                [empreendedor.email],  # Lista de destinatários
                fail_silently=False, # Se `False`, levanta um erro se o envio falhar
            )
            messages.success(request, "Um e-mail foi enviado com o link para redefinir sua senha.")
        except Empreendedor.DoesNotExist:
            messages.error(request, "E-mail não encontrado.")

    return render(request, "recuperarsenha.html")


def resetar_senha(request, token):
    """ Redefine a senha usando o token enviado no e-mail """
    if token not in reset_tokens:
        messages.error(request, "Token inválido ou expirado.")
        return redirect("recuperar_senha")

    email = reset_tokens.pop(token)  # Recupera e remove o token
    empreendedor = Empreendedor.objects.get(email=email)

    if request.method == "POST":
        nova_senha = request.POST.get("nova_senha")
        empreendedor.senha = criptografia(nova_senha)  # Criptografa a nova senha
        empreendedor.save()
        messages.success(request, "Senha alterada com sucesso! Faça login com a nova senha.")
        return redirect("login")

    return render(request, "resetarsenha.html", {"token": token})
    