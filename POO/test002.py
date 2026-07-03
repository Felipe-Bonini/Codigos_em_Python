class Aluno:
    def __init__(self, nome, nota):
        self.nome=nome
        self.nota=nota
    def situacao(self):
        if self.nota>=6:
            return "Aprovado!"
        elif self.nota>=4 and self.nota<6:
            return "Recuperacao!"
        elif self.nota<4:
            return "Reprovado!"
        else:
            return "Mencao invalida!"

a1=Aluno("Caio", 10)
a2=Aluno("Bonini", 5)

print(f"Aluno 1: {a1.nome}, nota: {a1.nota}, {a1.situacao()}")
print(f"Aluno 2: {a2.nome}, nota: {a2.nota}, {a2.situacao()}")