vNotas=[]
for i in range(5):
    notas=float(input("Digite uma nota"))
    vNotas.append(notas)

md=sum(vNotas)/len(vNotas)

print(md)