ano=int(input("Escreva o ano que voce quer descobrir se eh bissexto: "))
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("O ano eh BISSEXTO!")
else: 
    print("O ano nao eh Bissexto :(")