class Livro:
    def __init__(self, titulo, autor):
        self.titulo=titulo
        self.autor=autor
    def mostrar(self):
        print(f"Autor: {self.autor}. Titulo: {self.titulo}")

l1=Livro("Alienista", "Machado")
l2=Livro("Hora da Estrela", "Clarice")

l1.mostrar()
l2.mostrar()