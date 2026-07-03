user=str(input("Login: "))
if user=="admin":
    senha=int(input("Senha: "))
    if senha==1234:
        print("Acesso liberado!")
    else:
        print("Senha incorreta!")
else:
    print("Acesso negado!")