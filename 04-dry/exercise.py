from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum, auto
from typing import Iterable, TypedDict

from pydantic import BaseModel, EmailStr

SENDER_EMAIL = "sales@webshop.com"


class OrderType(StrEnum):
    ONLINE = "online"
    IN_STORE = "in store"


class EmailType(StrEnum):
    ORDER_CONFIRMATION = auto()
    ORDER_SHIPPED = auto()


class EmailContent(TypedDict):
    recipient: str
    sender: str
    body: str
    subject: str


@dataclass
class Item:
    name: str
    price: Decimal


@dataclass
class Order:
    id: int
    type: OrderType
    customer_email: str


class Email(BaseModel):
    body: str
    subject: str
    recipient: EmailStr
    sender: EmailStr


def calculate_total_price(items: Iterable[Item], discount: Decimal | None = None) -> Decimal:
    total_price = Decimal(sum(item.price for item in items))
    if discount is not None:
        total_price = total_price - (total_price * discount)
    return total_price


def _get_email_content(order: Order, email_type: EmailType) -> EmailContent:
    email_content = {
        "recipient": order.customer_email,
        "sender": SENDER_EMAIL,
    }

    custom_email_content = {
        EmailType.ORDER_CONFIRMATION: {
            "body": f"Thank you for your order! Your order #{order.id} has been confirmed.",
            "subject": "Order Confirmation",
        },
        EmailType.ORDER_SHIPPED: {
            "body": f"Good news! Your order #{order.id} has been shipped and is on its way.",
            "subject": "Order Shipped",
        },
    }

    email_content.update(**custom_email_content[email_type])

    return email_content


def generate_email(order: Order, email_type: EmailType) -> Email:
    email_content = _get_email_content(order, email_type)

    return Email(**email_content)


def process_order(order: Order) -> None:
    print(f"Processing {order.type} order...")
    print(generate_email(order, EmailType.ORDER_CONFIRMATION))

    if order.type == OrderType.ONLINE:
        process_online_order(order)
    elif order.type == OrderType.IN_STORE:
        process_in_store_order(order)
    else:
        raise ValueError(f"Invalid order type: {order.type}")

    print("Order processed successfully.")


def process_online_order(order: Order) -> None:
    print(f"Shipping the order {order.id}")
    print(generate_email(order, EmailType.ORDER_SHIPPED))


def process_in_store_order(order: Order) -> None:
    print(f"Order {order.id} is ready for pickup.")


def main() -> None:
    items = [
        Item(name="T-Shirt", price=Decimal("19.99")),
        Item(name="Jeans", price=Decimal("49.99")),
        Item(name="Shoes", price=Decimal("79.99")),
    ]

    online_order = Order(id=123, type=OrderType.ONLINE, customer_email="sarah@gmail.com")

    total_price = calculate_total_price(items)
    print("Total price:", total_price)

    discounted_price = calculate_total_price(items, Decimal("0.1"))
    print("Discounted price:", discounted_price)

    process_order(online_order)

    in_store_order = Order(id=456, type=OrderType.IN_STORE, customer_email="john@gmail.com")
    process_order(in_store_order)


if __name__ == "__main__":
    main()
