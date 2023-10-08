import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb

import pandas as pd
import presenter


class View:
    def __init__(self) -> None:
        self.presenter: presenter.Presenter
        self.master = tk.Tk()
        self.master.title("Data Analysis Tool")

        self.load_button = tk.Button(self.master, text="Load CSV", command=self.on_load_csv_button_click)
        self.show_input_data_button = tk.Button(
            self.master, text="Show input data", command=self.on_show_input_data_button_click
        )
        self.analyze_button = tk.Button(
            self.master,
            text="Analyze Data",
            command=self.on_analyze_data_button_click,
        )
        self.selected_option = tk.StringVar(self.master)
        self.options = ["All", "Temperature", "Humidity", "CO2"]
        self.selected_option.set(self.options[0])
        self.option_menu = tk.OptionMenu(self.master, self.selected_option, *self.options)

        self.export_button = tk.Button(
            self.master,
            text="Export Data",
            command=self.on_export_data_button_click,
        )
        self.text_widget = tk.Text(self.master)

        self.text_widget.pack(side=tk.BOTTOM)
        self.load_button.pack(side=tk.LEFT)
        self.show_input_data_button.pack(side=tk.LEFT)
        self.analyze_button.pack(side=tk.LEFT)
        self.option_menu.pack(side=tk.LEFT)
        self.export_button.pack(side=tk.LEFT)

    def set_data(self, data: pd.DataFrame) -> None:
        self.text_widget.delete("1.0", tk.END)
        try:
            self.text_widget.insert(tk.END, str(data))
        except NameError:
            mb.showinfo("Error", "No data to show!")

    def on_load_csv_button_click(self) -> None:
        file_path = fd.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.presenter.load_csv(file_path)
            mb.showinfo("Import", "Data successfully loaded!")
            self.show_input_data_button["state"] = "normal"
            self.analyze_button["state"] = "normal"
            self.export_button["state"] = "normal"

    def on_show_input_data_button_click(self) -> None:
        self.presenter.show_input_data()

    def on_analyze_data_button_click(self) -> None:
        self.presenter.analyze_data(self.selected_option.get())

    def on_export_data_button_click(self) -> None:
        file_path = fd.asksaveasfile(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")],
        )
        if file_path is not None:
            self.presenter.export_data(file_path)
            mb.showinfo("Export", "Data exported successfully!")
