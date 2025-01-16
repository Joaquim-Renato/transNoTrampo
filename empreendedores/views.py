from django.shortcuts import render, redirect
from .models import Empreendedor

# Create your views here.

def cadastrar_empreendedor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        idade = request.POST['idade']
        identidadegenero = request.POST['identidadegenero']
        email = request.POST['email']
        telefone = request.POST['telefone']
        servico = request.POST['servico']
        descricao = request.POST['descricao']

        if not nome or not email or not servico:
            return render(request, 'cadastrar.html', {'error': 'Preencha os campos obrigatórios.'})


        Empreendedor.objects.create(
        nome=nome, 
        idade =idade, 
        identidadegenero=identidadegenero, 
        email=email, 
        telefone=telefone, 
        servico=servico, 
        descricao=descricao
        )
        
        return redirect('lista_empreendedores')
    return render(request, 'cadastrar.html')


def lista_empreendedores(request):

    empreendedores = Empreendedor.objects.all()
    return render(request, 'lista.html', {'empreendedores': empreendedores})


def index(request):
    return render(request, 'index.html')  

def edit_empreendedor(request, id):
    empreendedor = Empreendedor.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST['nome']
        idade = request.POST['idade']
        identidadegenero = request.POST['identidadegenero']
        email = request.POST['email']
        telefone = request.POST['telefone']
        servico = request.POST['servico']
        descricao = request.POST['descricao']

        if not nome or not email or not servico:
            return render(
                request, 
                'editar.html', 
                {'empreendedor': empreendedor, 'error': 'Preencha os campos obrigatórios.'}
            )

        empreendedor.nome = nome
        empreendedor.idade = idade
        empreendedor.identidadegenero = identidadegenero
        empreendedor.email = email
        empreendedor.telefone = telefone
        empreendedor.servico = servico
        empreendedor.descricao = descricao
        empreendedor.save()

        return redirect('lista_empreendedores')
    
    return render(request, 'editar.html', {'empreendedor': empreendedor})



