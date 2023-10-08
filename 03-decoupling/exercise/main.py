from decimal import Decimal

from bank import CheckingAccount, SavingsAccount, deposit, withdraw
from stripe_service import StripePaymentService

API_KEY = "sk_test_1234567890"


def main() -> None:
    savings_account = SavingsAccount("SA001", Decimal("1000"))
    checking_account = CheckingAccount("CA001", Decimal("500"))

    payment_service = StripePaymentService()
    payment_service.set_api_key(API_KEY)

    deposit(Decimal("200"), savings_account, payment_service)
    deposit(Decimal("300"), checking_account, payment_service)

    withdraw(Decimal("100"), savings_account, payment_service)
    withdraw(Decimal("200"), checking_account, payment_service)

    print(f"Savings Account Balance: {savings_account.balance}")
    print(f"Checking Account Balance: {checking_account.balance}")


if __name__ == "__main__":
    main()
