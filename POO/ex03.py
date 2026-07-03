class Veiculo:
    def __init__(self, velocidade):
        self.velocidade=velocidade
    def mover(self):
        print("Seu veiculo esta se movendo!")

class Moto(Veiculo):
    def __init__(self, velocidade, marca):
        super().__init__(velocidade)
        self.marca=marca
    def mover(self):
        super().mover()
        print(f"Sua {self.marca} esta a {self.velocidade} km/h")

m1=Moto(100, "Harley")
m1.mover()