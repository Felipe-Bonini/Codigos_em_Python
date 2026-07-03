num=int(input("Escreva um numero inteiro: "))
if num%5==0 and num%3==0:
    print("Seu numero e divisivel por 3 e por 5!")
elif num%3==0:
    print("Seu numero e divisivel por 3!")
elif num%5==0:
    print("Seu numero e divisivel por 5!")
else:
    print("Seu numero nao e divisivel nem por 3 e nem por 5!")