from abc import ABC, abstractmethod

class Funcionario:
    def __init__(self, nome, salario=0):
        self.nome=nome
        self.salario=salario
    
    @abstractmethod
    def calcular_pagamento(self):
        pass

class FuncionarioTemporario(Funcionario):
    def __init__(self, nome, salario_por_hora, horas_trabalhadas):
        super().__init__(nome)
        self.salario_por_hora=salario_por_hora
        self.horas_trabalhadas=horas_trabalhadas
    def calcular_pagamento(self):
        return self.salario_por_hora*self.horas_trabalhadas
    
class FuncionarioIntegral(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal=salario_mensal
    def calcular_pagamento(self):
        return self.salario_mensal
    
ft=FuncionarioTemporario("Klebrioswaldiano", 15.78, 552)
fi=FuncionarioIntegral("Enzo", 3300.89)

print(f"Pagamento de {ft.nome}: {ft.calcular_pagamento()} R$")
print(f"Pagamento de {fi.nome}: {fi.calcular_pagamento()} R$")