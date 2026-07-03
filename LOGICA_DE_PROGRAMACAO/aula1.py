class Carro:
    def __init__(self, modelo):
        self.modelo = modelo;
        self.velocidade = 0

    def acelerar(self):
        print(self.velocidade)
        print("modelo",self.modelo)

    def frear(self):
        pass

    def acenderFarol (self):
        pass

car1 = Carro("fusca")
car2 = Carro("brasilia")

  