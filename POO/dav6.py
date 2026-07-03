class Livro:
    def __init__(self, nome, autor):
        self._nome=nome
        self._autor=autor
        self._disp=disp=True
    def get_emprestar(self):
        if self._disp:
            self._disp=False
            return "Livro emprestado com sucesso!"
        else:
            print("Livro ja emprestado!")
    def get_devolver(self):
        if not self._disp:
            self._disp=True
            return "Livro devolvido com sucesso!"
        else:
            print("Livro ja disponivel!")
    def __str__(self):
        status="Disponivel" if self._disp else "Emprestado"
        return f"Titulo: {self._nome}, Autor(a): {self._autor}, Status: {status}"
    
l1=Livro("Harry Potter", "J.K. Rowling")
print(l1)
l1.get_emprestar()
print(l1)