from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    def calcular_area(self):
        return self.altura*self.base
    
class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    def calcular_area(self):
        return (self.base*self.altura)/2
    
class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio=raio
    def calcular_area(self):
        return 3.14*(self.raio**2)

ret=Retangulo(3, 6)
tri=Triangulo(12, 6)
cir=Circulo(4)
print(f"Area do Retangulo: {ret.calcular_area():.2f}")
print(f"Area do Triangulo: {tri.calcular_area():.2f}")
print(f"Area do Circulo: {cir.calcular_area():.2f}")