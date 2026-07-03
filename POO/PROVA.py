class Personagem:
    def __init__(self, nome, vida):
        self.__nome=nome
        self.__vida=vida
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome=nome
    def get_vida(self):
        return self.__vida
    def set_vida(self, vida):
        self.__vida=vida
    
    def atacar(self):
        print ("O personagem atacou genericamente!")
    
class Guerreiro(Personagem):
    def __init__(self, nome, vida, pontos_forca):
        super().__init__(nome, vida)
        self.__pontos_forca=pontos_forca
    def get_pontos_forca(self):
        return self.__pontos_forca
    def set_pontos_forca(self, pontos_forca):
        self.__pontos_forca=pontos_forca
    
    def atacar(self):
        print (f"{self.get_nome} atacou FEROZMENTE!")
        
    
class Mago(Personagem):
    def __init__(self, nome, vida, pontos_magia):
        super().__init__(nome, vida)
        self.__pontos_magia=pontos_magia
    def get_pontos_magia(self):
        return self.__pontos_magia
    def set_pontos_magia(self, pontos_magia):
        self.__pontos_magia=pontos_magia