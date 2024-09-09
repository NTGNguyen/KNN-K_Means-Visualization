from src.constants import DRAW_POINTS_TEXT, NEXT_STEP_BUTTON_TEXT
import tkinter as tk
from tkinter import messagebox

from src.GUI.coordinate_system.coordinate_system import CoordinateSystem

from .form_frame import FormFrame

from .button import ButtonInFrame2


class MainPage(tk.Frame):
    """MainPage class heritant from Frame in tkinter modules

    Args:
        tk (Frame): Frame from Tkinter modules
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.coordinate_system: CoordinateSystem = CoordinateSystem(
            self, bg='white')
        self.coordinate_system.pack(fill=tk.BOTH, expand=True, padx=300)

        self.form_frame = FormFrame(self)
        self.form_frame.pack()
        # self.form_frame = tk.Frame(self)
        # self.form_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # self.label = tk.Label(self.form_frame, text="Number of Points:")
        # self.label.pack(side=tk.TOP, padx=5)

        # self.entry = tk.Entry(self.form_frame)
        # self.entry.pack(side=tk.TOP, padx=5)

        # self.button = tk.Button(
        #     self.form_frame, text="Draw Points", command=self.draw_points)
        # self.button.pack(side=tk.TOP, padx=5)
        self.add_points_button = ButtonInFrame2(DRAW_POINTS_TEXT, self.form_frame, self.draw_points)
        self.next_step_button = ButtonInFrame2(NEXT_STEP_BUTTON_TEXT, self.form_frame, self.start_algo)
        # self.next_step_button = tk.Button(
        #     self.form_frame, text="Next Step", command=self.start_algo)
        # self.next_step_button.pack(side=tk.TOP, padx=5)

    def draw_points(self) -> None:
        """Reads the number of clusters from the entry and draws them.

        Args:
            self(MainPage)

        Returns:
            None
        """
        try:
            num_points = int(self.form_frame.entry.get())
            if num_points > 0 and num_points < 6:
                self.coordinate_system.draw_random_points(num_points)
            else:
                messagebox.showerror(
                    "Invalid input", "Please enter a valid number of points.")
        except ValueError:
            messagebox.showerror(
                "Invalid input", "Please enter a valid number of points.")

    def start_algo(self):
        """Triggers the next step in the process.
        Args:
            self(MainPage)

        Returns:
            None
        """
        self.coordinate_system.start_algor()
