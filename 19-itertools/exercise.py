import itertools
import random
from collections import Counter
from dataclasses import dataclass

from faker import Faker


@dataclass
class Person:
    name: str
    age: int
    city: str
    country: str


# Instantiate the Faker module
fake = Faker()

# List of possible countries
countries = [
    "UK",
    "USA",
    "Japan",
    "Australia",
    "France",
    "Germany",
    "Italy",
    "Spain",
    "Canada",
    "Mexico",
]

# Generate 1000 random Person instances
PERSON_DATA: list[Person] = [
    Person(fake.name(), random.randint(18, 70), fake.city(), random.choice(countries)) for _ in range(1000)
]


def main() -> None:
    filtered_data = list(itertools.filterfalse(lambda user: user.age < 21, PERSON_DATA))

    summary = Counter([person.country for person in filtered_data])

    print(summary)


if __name__ == "__main__":
    main()
