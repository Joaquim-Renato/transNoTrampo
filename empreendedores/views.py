from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Empreendedor
from .forms import EmpreendedorSignUpForm

def cadastrar_empreendedor(request):
    if request.method == 'POST':
        form = EmpreendedorSignUpForm(request.POST)
        if form.is_valid():
            # Criação do usuário
            user = form.save()

            # Agora que o usuário está registrado, criamos o Empreendedor
            Empreendedor.objects.create(
                user=user, 
                idade=request.POST['idade'],
                identidadegenero=request.POST['identidadegenero'],
                telefone=request.POST['telefone'],
                servico=request.POST['servico'],
                descricao=request.POST['descricao']
            )

            # Efetuar login automaticamente após o cadastro
            login(request, user)

            messages.success(request, 'Cadastro realizado com sucesso! Você está logado agora.')
            return redirect('lista_empreendedores')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os campos.')
            return render(request, 'cadastrar.html', {'form': form})

    else:
        form = EmpreendedorSignUpForm()
    return render(request, 'cadastrar.html', {'form': form})

def lista_empreendedores(request):
    empreendedores = Empreendedor.objects.all()
    return render(request, 'lista.html', {'empreendedores': empreendedores})

def index(request):
    return render(request, 'index.html')

def edit_empreendedor(request, id):
    empreendedor = get_object_or_404(Empreendedor, id=id)

    # Certificando-se de que o usuário logado é o proprietário do empreendedor
    if empreendedor.user != request.user:
        return redirect('index')

    if request.method == 'POST':
        # Atualiza os campos do Empreendedor
        empreendedor.idade = request.POST['idade']
        empreendedor.identidadegenero = request.POST['identidadegenero']
        empreendedor.telefone = request.POST['telefone']
        empreendedor.servico = request.POST['servico']
        empreendedor.descricao = request.POST['descricao']
        empreendedor.save()

        messages.success(request, 'Dados atualizados com sucesso!')
        return redirect('lista_empreendedores')

    return render(request, 'editar.html', {'empreendedor': empreendedor})

def delete_empreendedor(request, id):
    empreendedor = get_object_or_404(Empreendedor, id=id)

    # Certificando-se de que o usuário logado é o proprietário do empreendedor
    if empreendedor.user != request.user:
        return redirect('index')

    if request.method == 'POST':
        empreendedor.delete()
        messages.success(request, 'Empreendedor excluído com sucesso!')
        return redirect('lista_empreendedores')

    return render(request, 'delete.html', {'empreendedor': empreendedor})
