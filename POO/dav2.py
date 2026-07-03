class Retangulo:
    def __init__(self, altura, largura):
        self.altura=altura
        self.largura=largura
    def area(self):
        return self.largura*self.altura
    def perimetro(self):
        return 2*(self.altura+self.largura)
    
retangulo = Retangulo(5.0, 3.0)

area = retangulo.area()
perimetro = retangulo.perimetro()

print(f"Área do retângulo: {area}")
print(f"Perímetro do retângulo: {perimetro}")