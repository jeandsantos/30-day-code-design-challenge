def count_fruits(fruits: list[str]) -> dict[str, int]:
    counter: dict[str, int] = {}

    for fruit in fruits:
        if fruit in counter:
            counter[fruit] += 1
        else:
            counter[fruit] = 1

    return counter


def main() -> None:
    result = count_fruits(
        [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    )

    print(result)

    assert result == {"apple": 4, "banana": 3, "cherry": 4}

    assert count_fruits([]) == {}
    # add more tests


if __name__ == "__main__":
    main()
