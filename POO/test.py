class Endereco:
    def __init__(self, cidade):
        self.cidade = cidade

class Pessoa:
    def __init__(self, nome, cidade):
        self.nome = nome
        self.endereco = Endereco(cidade)

p1 = Pessoa("Felipe", "São Paulo")

print(p1.nome)
print(p1.endereco.cidade)