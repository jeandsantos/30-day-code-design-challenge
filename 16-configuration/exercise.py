import json
from functools import partial
from string import Template
from typing import Any, Callable

import requests
from pydantic import BaseModel

HttpGet = Callable[[str], Any]

CONFIG_FILE = "config.json"


class Configs(BaseModel):
    api_key: str
    url_template: str


class CityNotFoundError(Exception):
    pass


def load_configs(file_path: str) -> Configs:
    with open(file_path, "r", encoding="utf-8") as file:
        configs_dict = json.load(file)

    configs = Configs(**configs_dict)

    return configs


def get(url: str) -> Any:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raise an exception if the request failed
    return response.json()


def get_forecast(http_get: HttpGet, configs: Configs, city: str) -> dict[str, Any]:
    url = Template(configs.url_template)
    response = http_get(url.substitute({"city": city, "api_key": configs.api_key}))
    if "main" not in response:
        raise CityNotFoundError(f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n")
    return response


def get_temperature(full_weather_forecast: dict[str, Any]) -> float:
    temperature = full_weather_forecast["main"]["temp"]
    return temperature - 273.15  # convert from Kelvin to Celsius


def get_humidity(full_weather_forecast: dict[str, Any]) -> int:
    return full_weather_forecast["main"]["humidity"]


def get_wind_speed(full_weather_forecast: dict[str, Any]) -> float:
    return full_weather_forecast["wind"]["speed"]


def get_wind_direction(full_weather_forecast: dict[str, Any]) -> int:
    return full_weather_forecast["wind"]["deg"]


def main() -> None:
    city = "Utrecht"

    configs = load_configs(CONFIG_FILE)

    get_weather = partial(get_forecast, get, configs)

    weather_forecast = get_weather(city)

    print(f"The current temperature in {city} is {get_temperature(weather_forecast):.1f} °C.")
    print(f"The current humidity in {city} is {get_humidity(weather_forecast)}%.")
    print(
        f"The current wind speed in {city} is {get_wind_speed(weather_forecast) } m/s from direction {get_wind_direction(weather_forecast)} degrees."
    )


if __name__ == "__main__":
    main()
