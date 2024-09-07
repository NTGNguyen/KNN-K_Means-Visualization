import tkinter as tk
from tkinter import messagebox
from src.GUI.coordinate_system.coordinate_system import CoordinateSystem

class MainPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller

        self.coordinate_system:CoordinateSystem = CoordinateSystem(self,bg='white')
        self.coordinate_system.pack(fill=tk.BOTH, expand=True,padx=300)

        self.form_frame = tk.Frame(self)
        self.form_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.label = tk.Label(self.form_frame, text="Number of Points:")
        self.label.pack(side=tk.TOP, padx=5)

        self.entry = tk.Entry(self.form_frame)
        self.entry.pack(side=tk.TOP, padx=5)

        self.button = tk.Button(self.form_frame, text="Draw Points", command  = self.draw_points)
        self.button.pack(side=tk.TOP, padx=5)

        self.next_step_button = tk.Button(self.form_frame, text="Next Step", command=self.start_algo)
        self.next_step_button.pack(side=tk.TOP, padx=5)

    def draw_points(self):
        """Reads the number of clusters from the entry and draws them."""
        try:
            num_points = int(self.entry.get())
            if num_points > 0 and num_points < 6:
                self.coordinate_system.draw_random_points(num_points)
            else:
                messagebox.showerror("Invalid input", "Please enter a valid number of points.")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number of points.")

    def start_algo(self):
        """Triggers the next step in the process."""
        self.coordinate_system.start_algor()

        
