import tkinter as tk
import random
from .clusters import ClusterDrawer
from .points import PointDrawer
from src.constants import COLORS
from src.utils.cal_mahattan_distance import manhattan_distance
from src.utils.average_coordinate import calculate_average
from .clusters import Cluster
from .points import Point

class CoordinateSystem(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.cluster_drawer = ClusterDrawer(self)
        self.point_drawer = PointDrawer(self)
        self.draw_coordinate_system()
        self.bind("<Configure>", self.on_resize)
        self.bind("<Button-1>", self.draw_cluster_on_click) 

    def draw_coordinate_system(self):
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()

        self.delete("all")

        width = self.winfo_width()
        height = self.winfo_height()

        self.create_line(50, height - 50, width - 50, height - 50, arrow=tk.LAST, fill="black") 
        self.create_line(50, height - 50, 50, 50, arrow=tk.LAST, fill="black")  

        step = 50
        for x in range(50, width - 50, step):
            self.create_line(x, height - 55, x, height - 45, fill="black")
            self.create_text(x, height - 40, text=str((x - 50) // step), anchor=tk.N)

        for y in range(height - 50 - step, 50, -step):
            self.create_line(45, y, 55, y, fill="black")
            self.create_text(40, y, text=str((height - 50 - y) // step), anchor=tk.E)

    def on_resize(self, event):
        self.draw_coordinate_system()

    def draw_cluster_on_click(self, event):
        """Handles mouse click events to draw a cluster (circle)."""
        x = event.x
        y = event.y
        self.cluster_drawer.draw_cluster(x, y,'white')

    def draw_random_points(self, num_points):
        """Draws a specified number of random points on the canvas."""
        width = self.winfo_width()
        height = self.winfo_height()
        self.point_drawer.clear_points()  
        
        for i in range(num_points):
            x = random.randint(50, width - 50)
            y = random.randint(50, height - 50)
            color = COLORS[i % len(COLORS)]  
            self.point_drawer.draw_point(x, y, color=color)
    def add_cluster(self, x, y, color):
        """Adds a cluster at (x, y) with the given color."""
        self.cluster_drawer.draw_cluster(x, y, color)
    
    def start_algor(self):
        coordinate_red_list = []
        coordinate_blue_list = []
        coordinate_orange_list = []
        coordinate_brown_list = []
        coordinate_green_list = []
        coordinate_lists = {
            "red": coordinate_red_list,
            "blue": coordinate_blue_list,
            "orange": coordinate_orange_list,
            "brown": coordinate_brown_list,
            "green": coordinate_green_list,
        }       
        clusters_data:list[Cluster] = self.cluster_drawer.get_clusters()
        points_data:list[Point] = self.point_drawer.get_point_data()
        for cluster in clusters_data:
            point_min_dis = min([(manhattan_distance(cluster.x,cluster.y,point.x,point.y),point.color) for point in points_data],key = lambda x:x[0])
            self.cluster_drawer.recolor_cluster(cluster_id=cluster.cluster_id,new_color= point_min_dis[1])
            cluster.color = point_min_dis[1]
            coordinate_lists[point_min_dis[1]].append([cluster.x,cluster.y])
        for point in points_data:
            coordinate_move = calculate_average(coordinate_lists[point.color])
            if coordinate_move!=None:
                self.point_drawer.move_point(point.point_id,coordinate_move[0],coordinate_move[1])
                point.x = coordinate_move[0]
                point.y = coordinate_move[1]
        

        
        

            
                
                

    
