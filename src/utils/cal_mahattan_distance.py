def manhattan_distance(x1, y1, x2, y2):
    """
    Calculate the Manhattan distance between two points in a 2D space.

    Parameters:
    x1 (float): The x-coordinate of the first point.
    y1 (float): The y-coordinate of the first point.
    x2 (float): The x-coordinate of the second point.
    y2 (float): The y-coordinate of the second point.

    Returns:
    float: The Manhattan distance between the two points.
    """
    return abs(x1 - x2) + abs(y1 - y2)
