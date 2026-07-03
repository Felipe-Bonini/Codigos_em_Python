from abc import ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def calcular_preco(self):
        pass
    @abstractmethod
    def descricao(self):
        pass

class Livro(Produto):
    def __init__(self, nome, autor, preco):
        self.nome=nome
        self.autor=autor
        self.preco=preco
    def calcular_preco(self):
        return self.preco
    def descricao(self):
        return f"Livro: {self.nome}, Autor: {self.autor}"
    
class Eletronico(Produto):
    def __init__(self, nome, marca, preco):
        self.nome=nome
        self.marca=marca
        self.preco=preco
    def calcular_preco(self):
        return self.preco
    def descricao(self):
        return f"Eletronico: {self.nome}, Marca: {self.marca}"
    
class Alimento(Produto):
    def __init__(self, nome, tipo, preco):
        self.nome=nome
        self.tipo=tipo
        self.preco=preco
    def calcular_preco(self):
        return self.preco
    def descricao(self):
        return f"Alimento: {self.nome}, Tipo: {self.tipo}"

l=Livro("Alienista", "Machado", 10)
e=Eletronico("Celular", "Samsung", 1299.99)
a=Alimento("Banana", "Fruta", 2)

print(l.descricao())
print(f"Preco: {l.calcular_preco():.2f} RS$")
print(e.descricao())
print(f"Preco: {e.calcular_preco():.2f} RS$")
print(a.descricao())
print(f"Preco: {a.calcular_preco():.2f} RS$")