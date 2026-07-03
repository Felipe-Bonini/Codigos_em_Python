vNome=[]
for i in range(5):
    alunos=str(input(f"Escreva o nome do {i+1} aluno: "))
    vNome.append(alunos)

vNome.sort()
print("Alunos:")
for aluno in vNome:
    print(aluno)