def calculate_average(coordinate_list) -> list[float] | None:
    """Function to Calculate the average of coordinate list

    Args:
        coordinate_list: list[list]

    Returns:
        List[float]: The Average Coordinate
    """
    if not coordinate_list:
        return None

    sum_x = sum(x for x, y in coordinate_list)
    sum_y = sum(y for x, y in coordinate_list)

    # Calculate the average
    avg_x = sum_x / len(coordinate_list)
    avg_y = sum_y / len(coordinate_list)

    return [avg_x, avg_y]
