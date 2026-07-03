saldo=5000
print(f"Seu saldo e de: {saldo}")
print(" ")
saq=float(input("Digite o valor do saque: "))
if saq>saldo:
    print("Saque negado!")
else:
    print("Saque permitido!")