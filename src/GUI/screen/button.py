"""Some Button Classes using in the python GUI"""
import tkinter as tk
from src.constants import START_BUTTON_TEXT

class ButtonInFrame2(tk.Button):
    """Button using in frame 2

    Args:
        tk (Button): The Button modules in tkinter
    """
    def __init__(self,text,controller,action):
        super().__init__(controller,text=text, command=action)
        self.pack(side=tk.TOP, padx=5)

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
        self.config(font=("Helvetica", 16))  
        self.pack(pady=20)
        self.target_frame = target_frame

    def on_click(self):
        self.controller.show_frame(self.target_frame)



