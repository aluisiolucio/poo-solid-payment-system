from payment_processor import PaymentProcessor
from payment import PaymentPix, PaymentCard, PaymentInvoice


def main():
    processor = PaymentProcessor()

    payment1 = PaymentPix(150.00)
    payment2 = PaymentCard(250.50)
    payment3 = PaymentInvoice(89.90)

    processor.add_payment(payment1)
    processor.add_payment(payment2)
    processor.add_payment(payment3)

    print("\nProcessando todos os payments:")
    processor.process_all()


if __name__ == "__main__":
    main()
