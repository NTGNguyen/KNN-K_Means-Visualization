"""The app construct to contains 2 frame"""
import tkinter as tk

from src.constants import ICON_IMG_PATH, TITLE

from .home_page import HomePage
from .main_page import MainPage


class App(tk.Tk):
    """App modules class heritant from Tk modules in tkinter

    Args:
        tk (Tk): Tk from Tkinter modules
    """

    def __init__(self) -> None:
        """Constructer of App Class"""
        super().__init__()
        self.iconphoto(True, tk.PhotoImage(file=ICON_IMG_PATH))
        self.title(TITLE)

        self.attributes('-fullscreen', True)
        self.bind("<Escape>", self.toggle_fullscreen)
        self.bind("<F11>", self.toggle_fullscreen)

        screen_width: int = self.winfo_screenwidth()
        screen_height: int = self.winfo_screenheight()
        width = int(screen_width * 0.6)
        height = int(screen_height * 0.6)

        x: int = (screen_width - width) // 2
        y: int = (screen_height - height) // 2
        self.geometry(f'{width}x{height}+{x}+{y}')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames: HomePage | MainPage = {}

        for F in (HomePage, MainPage):
            page_name = F.__name__
            frame: HomePage | MainPage = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("HomePage")

    def toggle_fullscreen(self, event=None) -> None:
        """Toggle to fullscreen when starting app

        Args:
            event : event to toggle (Default is None)

        Returns:
            None
        """
        self.attributes('-fullscreen', not self.attributes('-fullscreen'))

    def show_frame(self, page_name) -> None:
        """Show frame specific in page_name

        Args:
            page_name (str): the frame(page) name to show

        Return:
            None
        """
        frame: HomePage | MainPage = self.frames[page_name]
        frame.tkraise()
