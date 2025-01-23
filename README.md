# Algumas anotações :

## Instalando django:
````cmd
pip install django==3.2.9
````
## mysql:
````cmd
Pip install mysqlclient
````

## Criando um novo projeto Django

````cmd
django-admin startproject seu_projeto
````
## Criando app
````cmd
python manage.py startapp nomedoapp
````

## Executando o servidor local "roda"

````cmd
python manage.py runserver

````

# Para criar um superusuário, execute o seguinte comando:

````cmd
python manage.py createsuperuser

````
Acesse http://127.0.0.1:8000/admin



````` py
 <a href="{% url 'editempreendedor' empreendedor.id %}" class="btn btn-secondary">Editar</a>
                    <a href="{% url 'deletempreendedor' empreendedor.id %}" 
                       onclick="return confirm('Tem certeza que deseja excluir este empreendedor?');"
                       class="btn btn-danger">Excluir</a> *//

`````


Sobre o codigo 

Cadastro de usuário (empreendedor). 
**cadastrar.html**

Edição de dados do empreendedor (somente o próprio pode editar).
**editar.html**

Exclusão de dados do empreendedor (somente o próprio pode excluir).
**delete.html**
Exibição de todos os empreendedores.
**lista.html**


pip é o gerenciador de pacotes do python 

## Estrutura do Projeto:
**models.py** – Definindo os modelos.<br>
**forms.py** – Formulário para cadastro de usuário. <br>
**views.py** – Lógica de controle do fluxo. <br>
**templates** – Templates HTML para visualização. <br>
**urls.py** – Configuração das rotas. <br>
**admin.py** – Registro do modelo no Django Admin.




 <a href="{% url 'edit_empreendedor' empreendedor.id %}">Editar</a>
                            <a href="{% url 'delete_empreendedor' empreendedor.id %}">Excluir</a>