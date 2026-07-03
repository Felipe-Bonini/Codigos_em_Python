class Produto:
    def __init__(self, nome, preco):
        self.nome=nome
        self.preco=preco
    def descricao(self):
        return f"Nome: {self.nome}, Preco: {self.preco} RS$"

class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso, altura, largura):
        super().__init__(nome, preco)
        self.peso=peso
        self.altura=altura
        self.largura=largura
    def descricao(self):
        return super().descricao()+f", Peso: {self.peso} G, Altura: {self.altura} CM, Largura: {self.largura} CM"
    
class ProdutoDigital(Produto):
    def __init__(self, nome, preco, tamanho_arquivo):
        super().__init__(nome, preco)
        self.tamanho_arquivo=tamanho_arquivo
    def descricao(self):
        return super().descricao()+f", Tamanho do Arquivo: {self.tamanho_arquivo} MB"
    
pf=ProdutoFisico("Molho", 5, 200, 10, 3)
print(pf.descricao())
pd=ProdutoDigital("Livro", 20.50, 5)
print(pd.descricao())