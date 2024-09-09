"""The Start Button in main page"""
import tkinter as tk

from src.constants import START_BUTTON_TEXT


class StartButton(tk.Button):
    """The Start Button class heritant from Button in tk Modules

    Args:
        tk (Button): The Button modules in tkinter 
    """

    def __init__(self, parent, controller, target_frame):
        super().__init__(parent, text=START_BUTTON_TEXT, command=self.on_click)
        self.controller = controller
        self.pack(pady=20)
        self.target_frame = target_frame

    def on_click(self):
        self.controller.show_frame(self.target_frame)
