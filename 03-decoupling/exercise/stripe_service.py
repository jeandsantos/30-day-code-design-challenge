from dataclasses import dataclass

from service import PaymentService


@dataclass
class StripePaymentService(PaymentService):
    service_name: str = "Stripe"
    api_key: str | None = None

    def set_api_key(self, api_key: str) -> None:
        print(f"Setting Stripe API key to {api_key}.")
        self.api_key = api_key
