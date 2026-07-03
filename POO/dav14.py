class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo=modelo
        self.ano=ano
        self.preco=preco
    def calcularimposto(self):
        return 0.1*self.preco

class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca=marca
    def desconto(self):
        return 0.05*self.preco
    
class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada=cilindrada
    def calcularimposto(self):
        return 0.05*self.preco

car=Carro("Civic", 2008, 84999.90, "Honda")
mot=Moto("De veio", 2018, 55000.00, 67)

print(f"Imposto a ser pago do Carro: {car.calcularimposto()} R$")
print(f"Imposto a ser pago da Moto: {mot.calcularimposto()} R$")