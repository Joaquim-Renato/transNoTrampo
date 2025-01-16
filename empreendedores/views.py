from django.shortcuts import render, redirect
from .models import Empreendedor

# Create your views here.

def cadastrar_empreendedor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        idade = request.POST['idade']
        identidadedegenero = request.POST['identidadedegenero']
        email = request.POST['email']
        telefone = request.POST['telefone']
        servico = request.POST['servico']
        descricao = request.POST['descricao']

        Empreendedor.objects.create(
        nome=nome, idade =idade, 
        identidadedegenero=identidadedegenero, 
        email=email, telefone=telefone, 
        servico=servico, 
        descricao=descricao
        )
        
        return redirect('lista_empreendedores')
    return render(request, 'cadastrar.html')


def lista_empreendedores(request):
    empreendedor = Empreendedor.objects.all()
    return render(request, 'lista.html', {'empreendedor': empreendedor})

def index(request):
    return render(request, 'index.html')  

