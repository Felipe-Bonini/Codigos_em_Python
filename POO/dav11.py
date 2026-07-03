from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass
    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        return "Carro Acelerando!"
    def frear(self):
        return "Carro freando!"
    
class Moto(Veiculo):
    def acelerar(self):
        return "Moto acelerando!"
    def frear(self):
        return "Moto freando!"
    
class Caminhao(Veiculo):
    def acelerar(self):
        return "Caminhao acelerando!"
    def frear(self):
        return "Caminhao freando!"
    
c1=Carro()
m=Moto()
c2=Caminhao()

print(c1.acelerar())
print(c1.frear())
print()
print(m.acelerar())
print(m.frear())
print()
print(c2.acelerar())
print(c2.frear())