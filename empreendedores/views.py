from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Empreendedor
from .forms import EmpreendedorForm
from .utils import criptografia, verificar_senha


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


@login_required
def perfil_empreendedor(request, empreendedor_id):
    empreendedor = get_object_or_404(Empreendedor, id=empreendedor_id)
    return render(request, "perfil.html", {"empreendedor": empreendedor})


@login_required
def edit_empreendedor(request, id):
    empreendedor = get_object_or_404(Empreendedor, id=id)
    if empreendedor.user != request.user:
        return HttpResponseForbidden("Você não tem permissão para editar este recurso.")

    if request.method == "POST":
        formulario = EmpreendedorForm(request.POST, instance=empreendedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Dados atualizados com sucesso!")
            return redirect("lista_empreendedores")
        else:
            messages.error(request, "Erro ao atualizar os dados.")
    else:
        formulario = EmpreendedorForm(instance=empreendedor)
    return render(request, "editar.html", {"form": formulario})


@login_required
def delete_empreendedor(request, id):
    empreendedor = get_object_or_404(Empreendedor, id=id)
    if empreendedor.user != request.user:
        return HttpResponseForbidden("Você não tem permissão para excluir este recurso.")
    if request.method == "POST":
        empreendedor.delete()
        messages.success(request, "Empreendedor excluído com sucesso!")
        return redirect("lista_empreendedores")
    return render(request, "delete.html", {"empreendedor": empreendedor})


def lista_empreendedores(request):
    empreendedores = Empreendedor.objects.all()
    return render(request, "lista.html", {"empreendedores": empreendedores})


def index(request):
    return render(request, "index.html")
