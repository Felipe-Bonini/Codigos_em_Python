class Autor:
    def __init__(self, autor_nome):
        self.autor_nome=autor_nome
    
class Livro:
    def __init__(self, autor_nome, nome):
        self.nome=nome
        self.autor=Autor(autor_nome)

livro=Livro("C.S. Lewis", "Cristianismo Puro e Simples")
print(livro.autor.autor_nome())