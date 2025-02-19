from abc import ABC, abstractmethod


# Classe base para payment (Herança e Polimorfismo)
class Payment(ABC):
    def __init__(self, amount: float) -> None:
        self._amount = amount # Atributo protegido

    @abstractmethod
    def process_payment(self) -> None:
        raise NotImplementedError


# Implementação para payment via Pix (OCP e LSP)
class PaymentPix(Payment):
    def process_payment(self) -> None:
        print(f"Processando pagamento de R${self._amount:.2f} via Pix.")


# Implementação para payment via Cartão (OCP e LSP)
class PaymentCard(Payment):
    def process_payment(self) -> None:
        print(f"Processando pagamento de R${self._amount:.2f} via Cartão de Crédito.")


# Implementação para payment via Invoice (OCP e LSP)
class PaymentInvoice(Payment):
    def process_payment(self) -> None:
        print(f"Gerando boleto para pagamento de R${self._amount:.2f}.")
