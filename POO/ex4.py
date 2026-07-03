class Funcionario:
    def __init__(self, nome, salario):
        self.nome=nome
        self.salario=salario
    def mostrar_dados(self):
        return f"O funcionario, {self.nome}, recebe: {self.salario} R$."
f1=Funcionario("Carlos", 1500)
print(f1.mostrar_dados())

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus=bonus
    def salario_total(self):
        return self.salario+self.bonus
    def mostrar_dados(self):
        return f"O Gerente: {self.nome}, recebe, no total: {self.salario_total()} R$."
g1=Gerente("Paulo", 1500, 500)
print(g1.mostrar_dados())