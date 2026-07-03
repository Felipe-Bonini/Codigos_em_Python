class ContaBancaria:
    def __init__(self, numero_conta, titular_conta):
        self.numero_conta=numero_conta
        self.titular_conta=titular_conta
        self.saldo=0.0
    def depositar(self, valor):
        if valor>0:
            txt=f"Deposito de {valor} R$, para Conta: {self.numero_conta} realizado com sucesso!"
            self.saldo+=valor
            print(txt)
        else:
            print("Valor insuficiente para Deposito!")
    def sacar(self, valor):
        if valor>0:
            if valor<=self.saldo:
                print(f"Saque de {valor} R$, para Conta: {self.numero_conta} realizado com sucesso!")
                self.saldo-=valor
            else:
                print("Saldo insifucuente para saque!")
        else:
            print("O valor para saque deve ser maior que zero!")

conta = ContaBancaria(12345, "João da Silva")
print(f"Saldo inicial da conta de {conta.titular_conta}: R${conta.saldo}")

conta.depositar(1000)
print(f"Saldo após depósito: R${conta.saldo}")

conta.sacar(500)
print(f"Saldo após saque: R${conta.saldo}")
