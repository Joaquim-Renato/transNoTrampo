from django.contrib.auth.hashers import make_password

def criptografia(senha):
    return make_password(senha)
