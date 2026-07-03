print("Voce tem tres opcoes:")

print(" ")

print("Soma")
print("Subtracao")
print("Sair")

print(" ")

opr=str(input("Escolha qual operacao vai querer: "))
if opr=="Soma" or opr=="soma":
    so1=int(input("Escreva um numero inteiro para ser somado com o proximo:  "))
    so2=int(input("Escreva o segundo numero inteiro: "))
    soma=int(so1+so2)
    print(" ")
    print(f"O resultado da sua soma eh: {soma}")

elif opr=="Subtracao" or opr=="subtracao":
    su1=int(input("Escreva um numero inteiro para ser subtraido com o proximo:  "))
    su2=int(input("Escreva o segundo numero inteiro: "))
    sub=int(su1-su2)
    print(" ")
    print(f"O resultado da sua soma eh: {sub}")

elif opr=="Sair" or opr=="sair":
    print("Operacao finalizada sem ser concluida!")
else:
    print("Comando nao reconhecido!")