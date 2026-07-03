class Produto:
    def __init__(self, nome, preco):
        self._nome=nome
        if preco>0:
            self._preco=preco
        else:
            self._preco=0
    def set_preco(self, valor):
        if valor>0:
            self._preco=valor
        else:
            print("Valor Invalido!")
    def get_preco(self):
        return self._preco
    def mostrar(self):
        return f"O produto: {self._nome}, custa: {self.get_preco()}"

p1=Produto("Celular", 900)
p1.set_preco(800)
print(p1.mostrar())