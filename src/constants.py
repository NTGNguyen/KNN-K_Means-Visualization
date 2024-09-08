import sys

if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    BUNDLE_DIR: str = f"{sys._MEIPASS}/"
else:
    BUNDLE_DIR = ""


BANNER = """
██╗  ██╗███╗   ███╗███████╗ █████╗ ███╗   ██╗███████╗
██║ ██╔╝████╗ ████║██╔════╝██╔══██╗████╗  ██║██╔════╝
█████╔╝ ██╔████╔██║█████╗  ███████║██╔██╗ ██║███████╗
██╔═██╗ ██║╚██╔╝██║██╔══╝  ██╔══██║██║╚██╗██║╚════██║
██║  ██╗██║ ╚═╝ ██║███████╗██║  ██║██║ ╚████║███████║
╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
        ██╗  ██╗███╗   ██╗███╗   ██╗                 
        ██║ ██╔╝████╗  ██║████╗  ██║                 
        █████╔╝ ██╔██╗ ██║██╔██╗ ██║                 
        ██╔═██╗ ██║╚██╗██║██║╚██╗██║                 
        ██║  ██╗██║ ╚████║██║ ╚████║                 
        ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝      
"""
TITLE = "KNN/KMeans Clustering and Classification"
ICON_IMG_PATH = "assets/logo.png"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
START_BUTTON_TEXT = "Start"
RED = 'red'
BLUE = 'blue'
ORANGE = 'orange'
BROWN = 'brown4'
GREEN = 'green4'
COLORS = [RED, BLUE, ORANGE, BROWN, GREEN]
