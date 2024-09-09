"""The Home Page element(parent is app)"""
import tkinter as tk

from src.constants import BANNER_IMG_PATH_REMOVEBG

from .button import StartButton


class HomePage(tk.Frame):
    """HomePage class heritant from Frame in tkinter modules

    Args:
        tk (Frame): Frame from Tkinter modules
    """

    def __init__(self, parent, controller):
        """Constructer of App Class"""
        super().__init__(parent)
        self.controller = controller

        self.banner_image = tk.PhotoImage(file=BANNER_IMG_PATH_REMOVEBG)
        label = tk.Label(self, image=self.banner_image)
        label.pack(side="top", fill="both", expand=True)

        button = StartButton(self, controller, "MainPage")
        button.config(width=20, height=3)
        button.pack(side="bottom", pady=150)  
