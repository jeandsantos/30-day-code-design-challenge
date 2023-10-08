import pandas as pd
from app import process_data
from model import Model
from view import View


class Presenter:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def load_csv(self, file_path: str) -> None:
        self.model.data = pd.read_csv(file_path)

    def show_input_data(self) -> None:
        self.view.set_data(self.model.data)

    def analyze_data(self, selected_option: str) -> None:
        self.model.processed_data = process_data(self.model.data, selected_option)
        self.view.set_data(self.model.processed_data)

    def export_data(self, file_path: str) -> None:
        self.model.processed_data.to_csv(file_path)
