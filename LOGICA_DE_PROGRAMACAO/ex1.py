class  calculadora:
    def __init__(self, marca, serie):
        self.marca = marca
        self.serie = serie

    def somar(self, a, b):
        return a+b
    
    def subtrair(self, a , b):
        return a-b
    
    def multiplicar(self, a, b):
        return a*b
    
    def dividir(self, a, b):
        if b==0:
            return "Erro: Divisao por 0"
        return a/b
    
calc1 = calculadora("Dell", "1910")
calc2 = calculadora("HP", "1977")

print(f"Calculadora 1: {calc1.marca} - Série {calc1.serie}")
print("Soma:", calc1.somar(10, 5))
print("Subtração:", calc1.subtrair(10, 5))
print("Multiplicação:", calc1.multiplicar(10, 5))
print("Divisão:", calc1.dividir(10, 5))

print("\nCalculadora 2: {0} - Série {1}".format(calc2.marca, calc2.serie))
print("Soma:", calc2.somar(20, 4))
print("Subtração:", calc2.subtrair(20, 4))
print("Multiplicação:", calc2.multiplicar(20, 4))
print("Divisão:", calc2.dividir(20, 4))