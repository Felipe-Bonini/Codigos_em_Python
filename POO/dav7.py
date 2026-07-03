class Funcionario:
    def __init__(self, nome, cargo):
        self._nome=nome
        self._cargo=cargo
    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        self._nome=nome
    def get_cargo(self):
        return self._cargo
    def set_cargo(self, cargo):
        self._cargo=cargo
    def __str__(self):
        return f"Funcionario: {self._nome}, Cargo: {self._cargo}"

f1=Funcionario("Felipe", "Gerente")
print(f1)
f1.set_cargo("Programador")
print(f1)