from dataclasses import dataclass
from decimal import Decimal


@dataclass
class PaymentService:
    """Base Class for payment service"""

    service_name: str

    def process_payment(self, amount: Decimal) -> None:
        print(f"Processing payment of {amount} via {self.service_name}.")

    def process_payout(self, amount: Decimal) -> None:
        print(f"Processing payout of {amount} via {self.service_name}.")
