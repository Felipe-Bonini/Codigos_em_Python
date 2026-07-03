class Bateria:
    def carregar(self):
        print("Carregando")

class Celular:
    def __init__(self):
        self.bateria=Bateria()

c1=Celular()
print(c1.bateria.carregar())