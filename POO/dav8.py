class Compromisso:
    def __init__(self, data, desc):
        self._data=data
        self._desc=desc
    def get_data(self):
        return self._data
    def set_data(self, data):
        self._data=data
    def get_desc(self):
        return self._desc
    def set_desc(self, desc):
        self._desc=desc
    def __str__(self):
        return f"Dia: {self._data}, Descricao: {self._desc}"
    
c1=Compromisso(15, "Visitar meu amigo na casa dele!")
print(c1)
c1.set_data(22)
print(c1)