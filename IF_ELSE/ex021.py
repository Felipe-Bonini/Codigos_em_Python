ps=int(input("Escreva seu peso (em kg): "))
alt=float(input("Escreva sua altura (em METROS): "))
print(" ")
imc=float(ps/(alt**2))
if imc<18.5:
    print(f"Com IMC: {imc} voce esta ABAIXO DO PESO!")
elif imc<25:
    print(f"Com IMC: {imc} voce esta com PESO NORMAL!")
elif imc<30:
    print(f"Com IMC: {imc} voce esta com SOBREPESO!")
else:
    print(f"Com IMC: {imc} voce esta com OBESIDADE!")