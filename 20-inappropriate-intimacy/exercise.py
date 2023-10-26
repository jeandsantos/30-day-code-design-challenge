from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Location:
    id: int
    street: str
    postal_code: str
    city: str
    province: str
    latitude: float
    longitude: float


@dataclass
class Message:
    id: int
    message_id: str
    raw_data: str
    date: datetime
    priority: int
    geolocation: list[Location] = field(default_factory=list)


def generate_breadcrumbs(url: str, location: Location) -> dict[str, str]:
    breadcrumbs: dict[str, str] = {}

    if location.postal_code:
        breadcrumbs["postal_code_url"] = f"{url}/postal_code/{location.postal_code}/"
    if location.city:
        city_slug = location.city.lower().replace(" ", "-")
        breadcrumbs["city_url"] = f"{url}/region/{city_slug}/"
    if location.province:
        breadcrumbs["province_url"] = f"{url}/region/province/{location.province.lower()}/"

    return breadcrumbs


def main() -> None:
    MAIN_URL = "https://myapi.com"

    location = Location(
        id=1,
        street="123 Main St",
        postal_code="12345",
        city="New York",
        province="NY",
        latitude=40.7128,
        longitude=74.0060,
    )

    breadcrumbs = generate_breadcrumbs(MAIN_URL, location)
    print(breadcrumbs)


if __name__ == "__main__":
    main()
