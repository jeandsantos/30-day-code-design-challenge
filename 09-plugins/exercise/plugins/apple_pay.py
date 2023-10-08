from decimal import Decimal

from factory import payment_processor_factory


def process_payment_apple_pay(total: Decimal) -> None:
    device_id = input("Please enter your Apple Pay device ID: ")
    device_id_masked = device_id[-4:].rjust(len(device_id), "*")
    print(f"Processing Apple Pay payment of ${total:.2f} with device ID {device_id_masked}...")


def initialize() -> None:
    payment_processor_factory.register("apple_pay", process_payment_apple_pay)
