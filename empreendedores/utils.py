import bcrypt

def criptografia(senha):

    salt = bcrypt.gensalt()

    criptosenhas = bcrypt.hashpw(senha.encode('utf8'),salt)
    return criptosenhas.decode('utf-8')