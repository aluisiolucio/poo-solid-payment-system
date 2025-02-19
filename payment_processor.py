from typing import List
from payment import Payment


# Classe para o processamento de payments (SRP e DIP)
class PaymentProcessor:
    def __init__(self) -> None:
        self.__payments: List[Payment] = []

    def add_payment(self, payment: Payment) -> None:
        self.__payments.append(payment)

    def process_all(self) -> None:
        for payment in self.__payments:
            payment.process_payment()
