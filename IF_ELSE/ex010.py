n1=int(input("Escreva um numero inteiro: "))
n2=int(input("Escreva outro numero inteiro: "))
n3=int(input("Escreva mais um numero inteiro: "))

if n1>n2 and n1>n3:
    print(f"O maior numero e: {n1}")
elif n2>n1 and n2>n3:
    print(f"O maior numero e: {n2}")
else:
    print(f"O maior numero e: {n3}")