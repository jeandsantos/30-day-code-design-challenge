import argparse
import json
import os
from enum import StrEnum, auto
from typing import Any

from dotenv import load_dotenv
from weather import get_complete_forecast, get_humidity, get_temperature, get_wind_direction, get_wind_speed, http_get

load_dotenv()


class Condition(StrEnum):
    TEMPERATURE = auto()
    HUMIDITY = auto()
    WIND = auto()


class Language(StrEnum):
    ENGLISH = "en"
    DUTCH = "nl"


def construct_parser(texts: dict[str, Any]) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Get the current weather information for a city")
    parser.add_argument("city", help="Name of the city to get the weather information for")
    parser.add_argument(
        "-c",
        "--conditions",
        dest="conditions",
        metavar="CONDITION",
        nargs="+",
        default=["temperature"],
        choices=texts["conditions_all"]
        + texts["conditions_temperature"]
        + texts["conditions_humidity"]
        + texts["conditions_wind"],
        help=texts["help_condition"],
    )

    parser.add_argument(
        "--api-key",
        default=os.getenv("OPEN_WEATHER_API_KEY"),
        help="API key for the OpenWeatherMap API",
    )

    return parser


def fetch_conditions_from_args(arg_condition: str, texts: dict[str, Any]) -> list[Condition]:
    if arg_condition in texts["conditions_humidity"]:
        return [Condition.HUMIDITY]
    elif arg_condition in texts["conditions_wind"]:
        return [Condition.WIND]
    elif arg_condition in texts["conditions_temperature"]:
        return [Condition.TEMPERATURE]
    else:
        return [Condition.TEMPERATURE, Condition.HUMIDITY, Condition.WIND]


def print_condition(
    condition: Condition,
    city: str,
    weather_forecast: dict[str, Any],
    texts: dict[str, str],
) -> None:
    info = {
        "city": city,
        "temperature": get_temperature(weather_forecast),
        "humidity": get_humidity(weather_forecast),
        "wind_speed": get_wind_speed(weather_forecast),
        "wind_direction": get_wind_direction(weather_forecast),
    }
    print(texts[f"info_{condition.name.lower()}"].format(**info))


def main():
    with open("texts.json", "r") as file:
        texts_all_languages = json.load(file)

    texts = texts_all_languages[Language.ENGLISH.value]

    parser = construct_parser(texts)
    args = parser.parse_args()

    weather_forecast = get_complete_forecast(http_get, args.api_key, args.city)

    conditions = fetch_conditions_from_args(args.conditions, texts)
    for condition in conditions:
        print_condition(condition, args.city, weather_forecast, texts)


if __name__ == "__main__":
    main()
