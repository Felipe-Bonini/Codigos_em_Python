from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def emitir_som(self):
        pass
    @abstractmethod
    def mover(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "AU AU"
    def mover(self):
        return "Correr"

class Gato(Animal):
    def emitir_som(self):
        return "MIAU"
    def mover(self):
        return "Desfilando"
    
class Pato(Animal):
    def emitir_som(self):
        return "QUACK"
    def mover(self):
        return "Nadando"
    
c=Cachorro()
g=Gato()
p=Pato()

print (f"O cachorro faz: {c.emitir_som()}, Movendo-se: {c.mover()}.")
print (f"O Gato faz: {g.emitir_som()}, Movendo-se: {g.mover()}.")
print (f"O Pato faz: {p.emitir_som()}, Movendo-se: {p.mover()}.")
