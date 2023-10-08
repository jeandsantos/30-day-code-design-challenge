from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum

from service import PaymentService


class TransactionTypes(StrEnum):
    DEPOSIT = "Depositing"
    WITHDRAW = "Withdrawing"


@dataclass
class Account:
    account_number: str
    balance: Decimal
    type: str

    def deposit(self, amount: Decimal) -> None:
        self._report_transaction(amount, TransactionTypes.DEPOSIT)
        self.balance += amount

    def withdraw(self, amount: Decimal) -> None:
        self._report_transaction(amount, TransactionTypes.WITHDRAW)
        self.balance -= amount

    def _report_transaction(self, amount: Decimal, transaction_type: TransactionTypes) -> None:
        print(f"{transaction_type.value} {amount} into {self.type} Account {self.account_number}.")


@dataclass
class SavingsAccount(Account):
    type: str = "Savings"


@dataclass
class CheckingAccount(Account):
    type: str = "Checking"


def deposit(amount: Decimal, account: Account, payment_service: PaymentService) -> None:
    payment_service.process_payment(amount)
    account.deposit(amount)


def withdraw(amount: Decimal, account: Account, payment_service: PaymentService) -> None:
    payment_service.process_payout(amount)
    account.withdraw(amount)
