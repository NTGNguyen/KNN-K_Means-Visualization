import tkinter as tk

from src.constants import BANNER

from .start_button import StartButton


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text=BANNER)
        label.pack(pady=20)

        button = StartButton(self, controller, "MainPage")
        button.pack()
