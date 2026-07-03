vNum=[]
for i in range(10):
    num=int(input(f"Escreva o {i+1} numero inteiro: "))
    vNum.append(num)
    print("-----------------------------")
print(f"Numeros: {vNum}")
print("-----------------------------")
print(f"Maior numero: {max(vNum)}")
print("-----------------------------")
print(f"Menor numero: {min(vNum)}")
print("-----------------------------")
print(f"Soma numeros: {sum(vNum)}")
print("-----------------------------")
print(f"Media numeros: {sum(vNum)/len(vNum)}")