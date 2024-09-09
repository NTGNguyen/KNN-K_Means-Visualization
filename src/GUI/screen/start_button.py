"""The Start Button in main page"""
import tkinter as tk

from src.constants import START_BUTTON_TEXT


class StartButton(tk.Button):
    """The Start Button class heritant from Button in tk Modules

    Args:
        tk (Button): The Button modules in tkinter 
    """

    def __init__(self, parent, controller, target_frame):
        """The Start button Constructer

        Args:
            parent (Frame): The Frame contains Button   
            controller (App): The app controller this button
            target_frame (str): Name of target frame
        """
        super().__init__(parent, text=START_BUTTON_TEXT, command=self.on_click)
        self.controller = controller
        self.pack(pady=20)
        self.target_frame = target_frame

    def on_click(self):
        self.controller.show_frame(self.target_frame)
