import tkinter as tk

class ClusterDrawer:
    def __init__(self, canvas:tk.Canvas):
        self.canvas = canvas
        self.clusters:list[Cluster] = []  # List to keep track of cluster IDs and their positions

    def draw_cluster(self, x, y,color, radius=5):
        """Draws a cluster (circle) at (x, y) with the given radius and color."""
        cluster_id = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="black", fill=color)
        self.clusters.append(Cluster(cluster_id,x,y,color))

    def get_clusters(self):
        """Returns a list of cluster data (x, y, color)."""
        return self.clusters

    def recolor_cluster(self, cluster_id, new_color):
        """Updates the color of a cluster based on its ID."""
        self.canvas.itemconfig(cluster_id, fill=new_color)


class Cluster:
    def __init__(self,cluster_id,x,y,color):
        self.cluster_id = cluster_id
        self.x:float= x
        self.y:float =y
        self.color:str = color
