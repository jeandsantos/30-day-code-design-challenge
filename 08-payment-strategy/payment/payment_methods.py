from decimal import Decimal
from typing import Protocol


class PaymentProcessor(Protocol):
    def process_payment(self, total: Decimal) -> None:
        ...


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, total: Decimal) -> None:
        card_number = input("Please enter your credit card number: ")
        expiration_date = input("Please enter your credit card expiration date: ")
        ccv = input("Please enter your credit card CCV: ")
        card_number_masked = card_number[-4:].rjust(len(card_number), "*")
        ccv_masked = len(ccv) * "*"
        print(
            f"Processing credit card payment of ${total:.2f} with card number {card_number_masked} and expiration date {expiration_date} and CCV {ccv_masked}..."
        )


class PaypalProcessor(PaymentProcessor):
    def process_payment(self, total: Decimal) -> None:
        username = input("Please enter your PayPal username: ")
        password = input("Please enter your PayPal password: ")
        password_masked = len(password) * "*"
        print(f"Processing PayPal payment of ${total:.2f} with username {username} and password {password_masked}...")


class ApplePayProcessor(PaymentProcessor):
    def process_payment(self, total: Decimal) -> None:
        device_id = input("Please enter your Apple Pay device ID: ")
        device_id_masked = device_id[-4:].rjust(len(device_id), "*")
        print(f"Processing Apple Pay payment of ${total:.2f} with device ID {device_id_masked}...")


PAYMENT_PROCESSORS: dict[str, PaymentProcessor] = {
    "cc": CreditCardProcessor(),
    "paypal": PaypalProcessor(),
    "apple": ApplePayProcessor(),
}
