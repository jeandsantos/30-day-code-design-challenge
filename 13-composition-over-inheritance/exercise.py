import os
from dataclasses import dataclass
from string import Template
from typing import Any, Optional, Union

import requests
from dotenv import load_dotenv

load_dotenv()


class CityNotFoundError(Exception):
    pass


class MissingAPIKeyError(Exception):
    pass


API_URL_TEMPLATE = Template("http://api.openweathermap.org/data/2.5/weather?q=$city&appid=$api_key")
OPEN_WEATHER_API_KEY: Union[str, None] = os.getenv("OPEN_WEATHER_API_KEY")
KELVIN_TO_CELSIUS_CONV: float = 273.15


@dataclass
class WeatherRequest:
    api_key: str
    city: str

    def get_api_url(self) -> str:
        if self.api_key is None:
            raise MissingAPIKeyError("API Key is missing. Please provide an API key.")

        return API_URL_TEMPLATE.substitute({"city": self.city, "api_key": self.api_key})


@dataclass
class WeatherService:
    weather_request: Optional[WeatherRequest] = None

    def add_request(self, weather_request: WeatherRequest) -> None:
        self.weather_request = weather_request

    def retrieve_forecast(self) -> dict[str, Any]:
        response = requests.get(self.weather_request.get_api_url(), timeout=5).json()
        if "main" not in response:
            raise CityNotFoundError(
                f"Couldn't find weather data. Check '{self.weather_request.city}' if it exists and is correctly spelled.\n"
            )

        return response


@dataclass
class WeatherDisplay:
    weather_request: WeatherRequest
    weather_service: WeatherService

    def __post_init__(self) -> None:
        self.weather_service.add_request(self.weather_request)

    def display(self) -> None:
        self._get_forecast()
        temperature = self._get_temperature()
        city = self._get_city()

        print(f"The current temperature in {city} is {temperature:.1f} °C.")

    def _get_forecast(self) -> None:
        self.forecast = self.weather_service.retrieve_forecast()

    def _get_temperature(self) -> str:
        temperature = self.forecast["main"]["temp"] - KELVIN_TO_CELSIUS_CONV
        return temperature

    def _get_city(self) -> str:
        city = self.forecast["name"]
        return city


def main() -> None:
    city = "Utrecht"

    weather_display = WeatherDisplay(
        weather_request=WeatherRequest(OPEN_WEATHER_API_KEY, city),
        weather_service=WeatherService(),
    )
    weather_display.display()


if __name__ == "__main__":
    main()
