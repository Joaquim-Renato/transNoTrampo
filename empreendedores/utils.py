import bcrypt

def criptografia(senha):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode("utf-8"), salt).decode("utf-8")


def verificar_senha(senha_informada, senha_armazenada):
    return bcrypt.checkpw(senha_informada.encode("utf-8"), senha_armazenada.encode("utf-8"))
