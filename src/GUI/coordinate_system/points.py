class PointDrawer:
    def __init__(self, canvas):
        self.canvas = canvas
        self.points = []

    def draw_point(self, x, y, color: str = 'blue', radius=40):
        """Draws a point (larger circle) at (x, y) with the given radius and color."""
        point_id = self.canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius, outline=color, fill=color)
        self.points.append(Point(point_id, x, y, color))

    def clear_points(self):
        """Clears all points from the canvas and the list."""
        for point_id, _, _ in self.points:
            self.canvas.delete(point_id)
        self.points.clear()

    def get_point_data(self):
        """Returns a list of point data (x, y, color)."""
        return self.points

    def move_point(self, pid, new_x, new_y):
        radius = (self.canvas.coords(pid)[2] - self.canvas.coords(pid)[0]) / 2
        self.canvas.coords(pid, new_x - radius, new_y -
                           radius, new_x + radius, new_y + radius)


class Point:
    def __init__(self, point_id, x, y, color):
        self.point_id = point_id
        self.x = x
        self.y = y
        self.color = color
