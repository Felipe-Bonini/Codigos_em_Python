com=float(input("Escreva o valor da compra: "))
des = float(com-(com*0.1))
if com>100:
    print(f"Sua compra saiu no valor de: {des}")
else:
    print("Compra sem desconto!")