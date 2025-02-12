# Algumas anotações :

## ordem de elaboração de projeto:
Models --> criei modelos

utils.py -> criei utilitarios

views. py ->
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
## Comandos para Gerenciar o Banco de Dados:

Crie as migrações para o mysql com:
````cmd
python manage.py makemigrations

````

Aplique as migrações ao banco de dados com:
````cmd
python manage.py migrate
```` 

## Executando o servidor local "roda"

````cmd
python manage.py runserver

````

# Para implementar cryptogrtafia de senha :
Para verificar a versão do pacote bcrypt instalado no seu ambiente Python, você pode usar o seguinte comando no terminal:
````cmd
pip show bcrypt
````
ou para instalar :
````cmd
pip install bcrypt    
````

# Para criar um superusuário, execute o seguinte comando:

````cmd
python manage.py createsuperuser

````
Acesse http://127.0.0.1:8000/admin

## Para processamento de imgs 
````cmd
 python -m pip install Pillow
````



# Sobre o codigo

**cadastrar.html**
Cadastro de usuário (empreendedor). 

**editar.html**
Edição de dados do empreendedor (somente o próprio pode editar).

**delete.html**
Exclusão de dados do empreendedor (somente o próprio pode excluir).

**lista.html**
Exibição de todos os empreendedores.



pip é o gerenciador de pacotes do python 

## Estrutura do Projeto:
**models.py** – Definindo os modelos.<br>
**forms.py** – Formulário para cadastro de usuário. <br>
**views.py** – Lógica de controle do fluxo. <br>
**templates** – Templates HTML para visualização. <br>
**urls.py** – Configuração das rotas. <br>
**admin.py** – Registro do modelo no Django Admin.


## Links interessantes 
https://www.dicas-de-django.com.br/077-17-cadastro

https://github.com/grbalmeida/rede-social-django/blob/master/bookmarks/account/templates/registration/login.html



 <a href="{% url 'edit_empreendedor' empreendedor.id %}">Editar</a>
                            <a href="{% url 'delete_empreendedor' empreendedor.id %}">Excluir</a>

### O send_mail() é uma função do Django usada para enviar e-mails. No seu código, ele está sendo usado para enviar um e-mail com um link de redefinição de senha.

"Recuperação de Senha",  # Assunto do e-mail
    f"Olá, clique no link para redefinir sua senha: {reset_link}",  # Corpo do e-mail
    settings.DEFAULT_FROM_EMAIL,  # Remetente (configurado nas settings do Django)
    [empreendedor.email],  # Lista de destinatários
    fail_silently=False,  # Se `False`, levanta um erro se o envio falhar



Para implementação futura login com google  
https://console.cloud.google.com/auth/clients?project=enhanced-bebop-450717-q6

https://console.cloud.google.com/auth/overview?project=enhanced-bebop-450717-q6

https://medium.com/umcodigo/autentica%C3%A7%C3%A3o-com-google-no-django-5584458e1b4a


````py
    path('social-auth/', include('social_django.urls', namespace='social-auth')),
````




- password_reset envia o email
 - password_reset_done mostra uma mensagem de sucesso para o envio do email
 - password_reset_confirm checa a url e pergunta por uma nova senha
 - password_reset_complete mostra uma mensagem de sucesso para todo o processo


### algumas referecncias : 
 https://medium.com/umcodigo/autentica%C3%A7%C3%A3o-com-google-no-django-5584458e1b4a


https://docs.logto.io/pt-BR/tutorial/how-to-build-google-sign-in-with-python-and-logto