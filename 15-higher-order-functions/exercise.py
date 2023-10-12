import os
from functools import partial
from typing import Any, Callable

import requests
from dotenv import load_dotenv

load_dotenv()

ResponseType = dict[str, Any]
ClientFunction = Callable[[str], ResponseType]

API_KEY: str = os.getenv("OPEN_WEATHER_API_KEY")  # type: ignore
KELVIN_TO_CELSIUS_CONV: float = 273.15


class CityNotFoundError(Exception):
    pass


def get_response(url: str) -> ResponseType:
    response = requests.get(url, timeout=5)
    return response.json()


def get_url(city: str, api_key: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    return url


def get_forecast(client_func: ClientFunction, city: str, api_key: str) -> ResponseType:
    url = get_url(city, api_key)
    forecast = client_func(url)

    if "main" not in forecast:
        raise CityNotFoundError(f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n")
    return forecast


def get_temperature(forecast: ResponseType) -> float:
    temperature = forecast["main"]["temp"]
    return temperature - KELVIN_TO_CELSIUS_CONV


def get_humidity(forecast: ResponseType) -> int:
    return forecast["main"]["humidity"]


def get_wind_speed(forecast: ResponseType) -> float:
    return forecast["wind"]["speed"]


def get_wind_direction(forecast: ResponseType) -> int:
    return forecast["wind"]["deg"]


def display_forecast(forecast: ResponseType, city: str) -> None:
    temperature = get_temperature(forecast)
    humidity = get_humidity(forecast)
    wind_speed = get_wind_speed(forecast)
    wind_direction = get_wind_direction(forecast)

    print(f"The current temperature in {city} is {temperature:.1f} °C.")
    print(f"The current humidity in {city} is {humidity}%.")
    print(f"The current wind speed in {city} is {wind_speed} m/s from direction {wind_direction} degrees.")


def main() -> None:
    city = "Utrecht"

    get_weather = partial(get_forecast, client_func=get_response, api_key=API_KEY)
    forecast = get_weather(city=city)
    display_forecast(forecast, city)


if __name__ == "__main__":
    main()
