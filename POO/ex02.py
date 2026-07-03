class Conta:
    def __init__(self, saldo):
        self._saldo=saldo
    def depositar(self, valor):
        if valor>0:
            self._saldo=self._saldo+valor
    def sacar(self, valor):
        if valor>0 and valor<=self._saldo:
            self._saldo=self._saldo-valor
        else:
            print("Saque nao permitido!")
    def ver_saldo(self):
        return self._saldo
    
c1=Conta(200)
c1.sacar(100)
print(c1.ver_saldo())