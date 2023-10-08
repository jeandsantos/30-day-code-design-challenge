from enum import StrEnum
from typing import Callable

import pandas as pd


class Options(StrEnum):
    ALL = "All"
    TEMPERATURE = "Temperature"
    HUMIDITY = "Humidity"
    CO2 = "CO2"

    @classmethod
    def list(cls):
        return [c.value for c in cls]


TEMPERATURE_FACTOR: float = 273.15
HUMIDITY_FACTOR: float = 100.0
CO2_FACTOR: float = 23.0


def process_temperature(value: float) -> float:
    value += TEMPERATURE_FACTOR
    return value


def process_humidity(value: float) -> float:
    value /= HUMIDITY_FACTOR
    return value


def process_co2(value: float) -> float:
    value += CO2_FACTOR
    return value


PROCESS_FUNCTION: dict[str, Callable[[float], float]] = {
    "Temperature": process_temperature,
    "Humidity": process_humidity,
    "CO2": process_co2,
}


def read_data(filepath: str) -> pd.DataFrame:
    data = pd.read_csv(filepath)
    return data


def filter_data(data: pd.DataFrame, sensor: str) -> pd.DataFrame:
    data = data.loc[data["Sensor"] == sensor]
    return data


def check_option(option: str) -> bool:
    if option not in Options.list():
        print(f'Option "{option}" not valid, should be ({", ".join(Options.list())})')
        return False
    else:
        return True


def get_option() -> str:
    option = input(f'Please provide an option. Choose between: ({", ".join(Options.list())})\n ')
    return option


def process_row(row: pd.Series) -> pd.Series:
    sensor: str = row["Sensor"]
    value: float = row["Value"]
    row["Value"] = PROCESS_FUNCTION[sensor](value)

    return row


def process_data(data: pd.DataFrame) -> pd.DataFrame:
    processed_data = []

    for _, row in data.iterrows():
        processed_row = process_row(row)
        processed_data.append(processed_row)

    processed_data_df = pd.DataFrame(data=processed_data)

    return processed_data_df


def main() -> None:
    option = get_option()
    while not check_option(option):
        option = get_option()

    data = read_data("sensor_data.csv")

    if option != Options.ALL:
        data = filter_data(data, option)

    processed_data = process_data(data)

    print(processed_data)


if __name__ == "__main__":
    main()
