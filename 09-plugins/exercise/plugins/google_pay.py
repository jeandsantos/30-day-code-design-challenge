from decimal import Decimal

from factory import payment_processor_factory


def process_payment_google_pay(total: Decimal) -> None:
    account_id = input("Please enter your Google account: ")
    account_id_masked = account_id[-4:].rjust(len(account_id), "*")
    print(f"Processing Google Pay payment of ${total:.2f} with device ID {account_id_masked}...")


def initialize() -> None:
    payment_processor_factory.register("google_pay", process_payment_google_pay)
