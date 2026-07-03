class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
    def descricao(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, qt_portas):
        super().__init__(marca, modelo, ano)
        self.qt_portas=qt_portas
    def descricao(self):
        return super().descricao()+f", Numero de Portas: {self.qt_portas}"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, modelo_motor):
        super().__init__(marca, modelo, ano)
        self.modelo_motor=modelo_motor
    def descricao(self):
        return super().descricao()+f", Modelo Motor: {self.modelo_motor}"
    
car=Carro("Honda", "Civic", 2000, 4)
moto=Moto("Harley", "Boa", 2010, "Muito Bom")
print(car.descricao())
print(moto.descricao())