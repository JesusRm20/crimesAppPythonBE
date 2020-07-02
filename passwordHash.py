from passlib.hash import sha256_crypt

def hashPassword(pwd):
    passwd = sha256_crypt.hash(str(pwd))

    return passwd

def passwordCheck(pwd, hashedpwd):

    password = pwd.encode('utf-8')
    resp = sha256_crypt.verify(password, hashedpwd)
    if resp:
        return True
    else:
        return False
