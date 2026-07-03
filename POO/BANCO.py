class ContaBancaria:
    def __init__(self, saldo):
        self._saldo=saldo
    def depositar(self, valor):
        if valor>0:
            self._saldo+=valor
    def sacar(self, valor):
        if valor>0 and valor<=self._saldo:
            self._saldo-=valor
        else:
            print("Valor Invalido!")
    def ver_saldo(self):
        return self._saldo
    
class ContaPremium(ContaBancaria):
    def __init__(self, saldo):
        super().__init__(saldo)
    def sacar(self, valor):
        #return super().sacar(valor)
        if valor>0 and valor<=self._saldo+50:
            self._saldo-=valor
        else:
            print("Valor Invalido!")

CB1=ContaBancaria(5000)
CB1.depositar(200)
print(CB1.ver_saldo())
CP1=ContaPremium(5000)
CP1.sacar(5049)
print(CP1.ver_saldo())