class Celular:
    def __init__(self, modelo, bateria):
        self.modelo=modelo
        self.bateria=bateria
    def usar(self):
        self.bateria=self.bateria-5
        if self.bateria<0:
            self.bateria=0
    def carregar(self):
        self.bateria=self.bateria+10
        if self.bateria>100:
            self.bateria=100

cel1=Celular("Iphone", 80)
cel1.usar()
print(f"Celular: {cel1.modelo}, bateria: {cel1.bateria}%")
cel1.usar()
print(f"Celular: {cel1.modelo}, bateria: {cel1.bateria}%")
cel1.carregar()
print(f"Celular: {cel1.modelo}, bateria: {cel1.bateria}%")
cel1.carregar()
print(f"Celular: {cel1.modelo}, bateria: {cel1.bateria}%")
cel1.usar()
print(f"Celular: {cel1.modelo}, bateria: {cel1.bateria}%")
cel1.carregar()
print(f"Celular: {cel1.modelo}, bateria: {cel1.bateria}%")
cel1.carregar()
print(f"Celular: {cel1.modelo}, bateria: {cel1.bateria}%")