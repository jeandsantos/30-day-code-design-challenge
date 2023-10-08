from dataclasses import dataclass, field
from decimal import Decimal


class ItemNotFoundException(Exception):
    pass


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    @property
    def subtotal(self) -> Decimal:
        return self.price * self.quantity


@dataclass
class Discount:
    amount: Decimal | None = None
    percentage: Decimal | None = None


DISCOUNTS = {
    "SAVE10": Discount(percentage=Decimal("0.1")),
    "5BUCKSOFF": Discount(amount=Decimal("5.00")),
    "FREESHIPPING": Discount(amount=Decimal("2.00")),
    "BLKFRIDAY": Discount(percentage=Decimal("0.2")),
}


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discounts: list[str] = field(default_factory=list)
    total_discount: Decimal = Decimal("0.00")

    def __post_init__(self) -> None:
        self.subtotal: Decimal = Decimal(sum(item.subtotal for item in self.items))
        self._apply_discounts()

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        found_item = self.find_item(item_name)
        self.items.remove(found_item)

    def find_item(self, item_name: str) -> Item:
        for item in self.items:
            if item.name == item_name:
                return item
        raise ItemNotFoundException(f"Item '{item_name}' not found.")

    def _apply_discounts(self) -> None:
        for discount_code in self.discounts:
            discount: Discount = DISCOUNTS[discount_code]

            if discount.percentage is not None:
                self.total_discount += Decimal(discount.percentage * self.subtotal)
            elif discount.amount is not None:
                self.total_discount += Decimal(discount.amount)
            else:
                raise ValueError("Invalid discount value")

    def display(self) -> None:
        print("Shopping Cart:")
        print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
        for item in self.items:
            print(f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}")
        print("=" * 40)
        print(f"Subtotal: ${self.subtotal:>7.2f}")
        print(f"Discount: ${self.total_discount:>7.2f}")
        print(f"Total:    ${self.total:>7.2f}")

    @property
    def total(self) -> Decimal:
        return self.subtotal - self.total_discount


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.50"), 10),
            Item("Banana", Decimal("2.00"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
        discounts=["SAVE10", "5BUCKSOFF"],
    )

    cart.display()


if __name__ == "__main__":
    main()
