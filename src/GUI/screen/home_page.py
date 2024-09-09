"""The Home Page element(parent is app)"""
import tkinter as tk

from src.constants import BANNER

from .start_button import StartButton



class HomePage(tk.Frame):
    """HomePage class heritant from Frame in tkinter modules

    Args:
        tk (Frame): Frame from Tkinter modules
    """

    def __init__(self, parent, controller):
        """Constructer of App Class"""
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text=BANNER)
        label.pack(pady=20)

        button = StartButton(self, controller, "MainPage")
        button.pack()
