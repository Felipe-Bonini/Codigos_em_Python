from abc import ABC, abstractmethod

class FormaPagamento(ABC):
    @abstractmethod
    def calcular_desconto(self, valor):
        pass
    @abstractmethod
    def calcular_parcelas(self, valor, qt_parcelas):
        pass

class CartaoCredito(FormaPagamento):
    def calcular_desconto(self, valor):
        return valor*0.05
    def calcular_parcelas(self, valor, qt_parcelas):
        return valor/qt_parcelas
    
class Boleto(FormaPagamento):
    def calcular_desconto(self, valor):
        return valor*0.07
    def calcular_parcelas(self, valor, qt_parcelas):
        return valor/qt_parcelas
    
class Transferencia(FormaPagamento):
    def calcular_desconto(self, valor):
        return valor*0.03
    def calcular_parcelas(self, valor, qt_parcelas):
        return valor/qt_parcelas
    
c=CartaoCredito()
b=Boleto()
t=Transferencia()

valor_compra=700.00
n_parcelas=12

desc_cartao=c.calcular_desconto(valor_compra)
parc_cartao=c.calcular_parcelas(valor_compra, n_parcelas)

desc_boleto=b.calcular_desconto(valor_compra)
parc_boleto=b.calcular_parcelas(valor_compra, n_parcelas)

desc_transferencia=t.calcular_desconto(valor_compra)
parc_transferencia=t.calcular_parcelas(valor_compra, n_parcelas)

print(f"Pagar com Cartao de Credito:\nDesconto: {desc_cartao:.2f} R$\nValor Parcelas: {parc_cartao:.2f} R$")
print(f"\nPagar com Boleto:\nDesconto: {desc_boleto:.2f} R$\nValor Parcelas: {parc_boleto:.2f} R$")
print(f"\nPagar com Transferencia:\nDesconto: {desc_transferencia:.2f} R$\nValor Parcelas: {parc_transferencia:.2f} R$")