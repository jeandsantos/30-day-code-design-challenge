import pandas as pd


class Model:
    def __init__(self) -> None:
        self.__data: pd.DataFrame = pd.DataFrame()
        self.__processed_data: pd.DataFrame = pd.DataFrame()

    @property
    def data(self) -> pd.DataFrame:
        return self.__data

    @data.setter
    def data(self, value: pd.DataFrame) -> None:
        self.__data = value

    @property
    def processed_data(self) -> pd.DataFrame:
        return self.__processed_data

    @processed_data.setter
    def processed_data(self, value: pd.DataFrame) -> None:
        self.__processed_data = value
