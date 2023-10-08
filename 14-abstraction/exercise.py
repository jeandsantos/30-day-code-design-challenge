import os
from dataclasses import dataclass
from string import Template
from typing import Any, Protocol, Union

import requests
from dotenv import load_dotenv

load_dotenv()

NumericType = Union[int, float]
ResponseType = dict[str, Any]

API_URL_TEMPLATE = Template("http://api.openweathermap.org/data/2.5/weather?q=$city&appid=$api_key")
OPEN_WEATHER_API_KEY: str = os.getenv("OPEN_WEATHER_API_KEY")  # type: ignore
KELVIN_TO_CELSIUS_CONV: float = 273.15


class CityNotFoundError(Exception):
    pass


class HttpClient(Protocol):
    def get(self, url: str) -> ResponseType:
        ...


@dataclass
class RequestsClient(HttpClient):
    def get(self, url: str) -> ResponseType:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        return response.json()


@dataclass
class WeatherService:
    requests_client: RequestsClient
    api_key: str

    def display_forecast(self, city: str) -> None:
        url = self.get_url(city)
        full_weather_forecast = self.requests_client.get(url)
        temp, hum, wind_speed, wind_direction = self._get_weather_data(full_weather_forecast)

        print(f"The current temperature in {city} is {temp:.1f} °C.")
        print(f"The current humidity in {city} is {hum}%.")
        print(f"The current wind speed in {city} is {wind_speed} m/s from direction {wind_direction} degrees.")

    def _get_weather_data(self, forecast: ResponseType) -> tuple[NumericType, NumericType, NumericType, NumericType]:
        temp = self._get_temp(forecast)
        hum = self._get_hum(forecast)
        wind_speed = self._get_wind_speed(forecast)
        wind_direction = self._get_wind_direction(forecast)

        return temp, hum, wind_speed, wind_direction

    def _get_temp(self, forecast: ResponseType) -> NumericType:
        temp = forecast["main"]["temp"] - KELVIN_TO_CELSIUS_CONV
        return temp

    def _get_hum(self, forecast: ResponseType) -> NumericType:
        hum = forecast["main"]["humidity"]
        return hum

    def _get_wind_speed(self, forecast: ResponseType) -> NumericType:
        wind_speed = forecast["wind"]["speed"]
        return wind_speed

    def _get_wind_direction(self, forecast: ResponseType) -> NumericType:
        wind_direction = forecast["wind"]["deg"]
        return wind_direction

    def get_url(self, city: str) -> str:
        return API_URL_TEMPLATE.substitute({"city": city, "api_key": self.api_key})


def main() -> None:
    city = "Utrecht"

    client = WeatherService(
        RequestsClient(),
        OPEN_WEATHER_API_KEY,
    )
    client.display_forecast(city)


if __name__ == "__main__":
    main()
