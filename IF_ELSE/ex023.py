senha=str(input("Escreva a senha: "))
num=False
for letra in senha:
    if letra.isdigit():
        num=True
if len(senha)>=8 and num:
    print("Senha forte!")
else: 
    print("Senha fraca!")