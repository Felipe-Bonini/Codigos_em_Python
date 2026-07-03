class Veiculo:
    def __init__(self, velocidade):
        self.velocidade=velocidade
    def acelerar(self):
        self.velocidade=self.velocidade+5
    def frear(self):
        self.velocidade=self.velocidade-5
        if self.velocidade<0:
            self.velocidade=0
    def mover(self):
        print("O veiculo esta se movendo!")

class Carro(Veiculo):
    def __init__(self, velocidade, marca):
        super().__init__(velocidade)
        self.marca=marca
    def mover(self):
        print(f"O {self.marca} esta a {self.velocidade} km/h!")

c1=Carro(100, "Honda")

print(c1.velocidade)  # 100
print(c1.marca)       # Honda

c1.acelerar()
print(c1.velocidade)  # 105

c1.frear()
print(c1.velocidade)  # 100

c1.mover()

#v1=veiculo(80)
#c1=carro(100)
#c1.frear()
#c1.frear()
#c1.frear()
#print(f"Velocidade do carro: {c1.velocidade}")
#v1.mover()
#c1.mover()
