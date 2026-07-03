l1=float(input("Escreva o tamamnho do 1o lado do triangulo: "))
l2=float(input("Escreva o tamamnho do 2o lado do triangulo: "))
l3=float(input("Escreva o tamamnho do 3o lado do triangulo: "))

if l1==l2 and l1==l3:
    print("Seu triangulo eh equilatero!")
elif l1==l2 or l1==l3 or l2==l3:
    print("Seu triangulo eh isosceles!")
else:
    print("Seu triangulo eh escaleno!")