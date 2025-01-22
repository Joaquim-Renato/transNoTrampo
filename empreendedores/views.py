from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Empreendedor
from .forms import EmpreendedorForm
from django.http import HttpResponse
from .utils import criptografia


def cadastrar_empreendedor(request):
    if request.method == "POST": 
         formulario = EmpreendedorForm(request.POST)
         
         print(formulario)
         
         if formulario.is_valid():
            empreendedor = formulario.save(
                commit=False
            )  # Cria o objeto, mas ainda não salva no banco de dados

            # Aqui aplica a criptografia na senha
            senha = formulario.cleaned_data.get("senha")
            senha_criptografada = criptografia(senha)  # Aplica a criptografia

             # Atualiza a senha criptografada no objeto do paciente
            empreendedor.senha = senha_criptografada

            empreendedor.save()  # Agora salva o com a senha criptografada

            messages.success(request, "Empreendedor cadastrado com sucesso!")
            return redirect("login")  # Redireciona para outra página
         
    else:

            messages.error(request, "Erro ao cadastrar. Verifique os dados informados.")
            
        # Inicializa o formulário vazio para requisições GET
    formulario = EmpreendedorForm()

    # O formulário estará sempre inicializado antes de renderizar o template
    return render(request, "cadastrar.html", {"form": formulario})
    


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
