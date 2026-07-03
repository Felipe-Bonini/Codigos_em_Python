class Carro:
    def __init__(self, marca, velocidade):
        self.marca=marca
        self.velocidade=velocidade
    def acelerar(self):
        self.velocidade=self.velocidade+10
    def frear(self):
        self.velocidade=self.velocidade-10
        if self.velocidade<0:
            self.velocidade=0

c1=Carro("Honda", 200)
c1.acelerar()
print(f"Primeiro carro: {c1.marca}, {c1.velocidade}")
c1.acelerar()
print(f"Primeiro carro: {c1.marca}, {c1.velocidade}")
c1.frear()
print(f"Primeiro carro: {c1.marca}, {c1.velocidade}")