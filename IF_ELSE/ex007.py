sal=float(input("Escreva o seu salario: "))
au1 = float(sal+(sal*0.2))
au2 = float(sal+(sal*0.1))
if sal<2000:
    print(f"Seu novo salario eh de: {au1}")
else:
    print(f"Seu novo salario eh de: {au2}")