#ABSTRACAO
from abc import ABC, abstractmethod

#ABSTRACAO
class Funcionario(ABC):
    #ENCAPSULAMENTO
    def __init__(self, nome, salario):
        self._nome=nome
        self._salario=salario
    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        self._nome=nome
    def get_salario(self):
        return self._salario
    def set_salario(self, salario):
        self._salario=salario
    
    #ABSTRACAO
    @abstractmethod
    def calcular_bonus(self):
        pass

#HERANCA
class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    def calcular_bonus(self):
        return self._salario*0.20

#HERANCA   
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    def calcular_bonus(self):
        return self._salario*0.10

#HERANCA    
class Estagiario(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    def calcular_bonus(self):
        return self._salario*0.05

#POLIMORFISMO
funcionarios=[Gerente("Rogerio", 5000), Desenvolvedor("Felipe", 3000), Estagiario("Lucas", 2000)]

for f in funcionarios:
    print(f"Nome: {f.get_nome()}\nSalario: {f.get_salario()}\nBonus: {f.calcular_bonus()}\n")