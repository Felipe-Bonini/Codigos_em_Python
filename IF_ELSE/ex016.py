nota=float(input("Escreva sua nota: "))
if nota>10:
    print("Novo einstein?")
elif nota<0:
    print("Novo nietsnie?")
elif nota<=4:
    print("Reprovado!")
elif nota>=7:
    print("Aprovado!")

else: 
    print("Recuperacao!")