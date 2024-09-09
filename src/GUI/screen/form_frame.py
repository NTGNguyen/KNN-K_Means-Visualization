"""The Form to input num of points"""
import tkinter as tk


class FormFrame(tk.Frame):
    """The Form Class

    Args:
        tk (Frame): Frame modules in tkinter
    """

    def __init__(self, controller):
        super().__init__(controller)
        self.pack(side=tk.RIGHT, padx=10, pady=10)

        self.label = tk.Label(self, text="Number of Points:")
        self.label.pack(side=tk.TOP, padx=5)

        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.TOP, padx=5)
