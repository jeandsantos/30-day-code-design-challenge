from math import pi
from typing import Union


def area_circle(radius: float):
    return pi * radius**2


def perimeter_circle(radius: float):
    return 2 * pi * radius


def area_rectangle(width: float, height: Union[float, None] = None):
    if height is None:
        height = width
    return width * height


def perimeter_rectangle(width: float, height: Union[float, None] = None):
    if height is None:
        height = width
    return 2 * (width + height)


def main() -> None:
    print(
        "Total Area:",
        sum(
            [
                area_rectangle(4, 5),
                area_rectangle(3),
                area_circle(2),
            ]
        ),
    )
    print(
        "Total Perimeter:",
        sum(
            [
                perimeter_rectangle(4, 5),
                perimeter_rectangle(3),
                perimeter_circle(2),
            ]
        ),
    )


if __name__ == "__main__":
    main()
