from decimal import Decimal

from factory import payment_processor_factory


def process_payment_paypal(total: Decimal) -> None:
    username = input("Please enter your PayPal username: ")
    password = input("Please enter your PayPal password: ")
    password_masked = len(password) * "*"
    print(f"Processing PayPal payment of ${total:.2f} with username {username} and password {password_masked}...")


def initialize() -> None:
    payment_processor_factory.register("paypal", process_payment_paypal)
