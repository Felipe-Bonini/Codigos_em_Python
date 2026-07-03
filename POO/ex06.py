class Carro:
    def mover(self):
        return "O carro esta se movendo!"

class Moto:
    def mover(self):
        return "A moto esta se movendo!"
    
veiculos=[Carro(), Moto()]

for f in veiculos:
    print(f.mover())
    