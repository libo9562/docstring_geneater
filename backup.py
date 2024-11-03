def calculate_area(radius: float, pi: float) -> float:
    """
    Calculate the area of a circle given its radius and the mathematical constant pi.

    Args:
        radius (float): The radius of the circle.
        pi (float): The mathematical constant pi.

    Returns:
        float: The calculated area of the circle.
    """
    return pi * radius * radius


def calculate_area1(radius: float, pi) -> float:
    """
    Calculates the area of a circle using its radius and a given approximation of PI.

    Args:
        radius (float): The radius of the circle.
        pi (float, optional): An approximation of PI (Defaults to 3.14159).
    """
    return pi * radius * radius


def calculate_area2(radius, pi) -> float:
    """
    Calculates the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.
        pi (float, optional): The value of pi to use in calculations. Defaults to 3.14159.

    Returns:
        float: The calculated area of the circle.
    """
    return pi * radius * radius


def calculate_area3(radius: float, pi: float):
    """
    Calculate the area of a circle.

    Returns:
        float: The calculated area of the circle using the formula A = πr².
    """
    return pi * radius * radius


def calculate_area4(radius, pi) -> float:
    """
    Calculates the area of a circle using the formula A = πr².

    Args:
        radius (float): The radius of the circle.
        pi (float): The value of pi. Defaults to 3.14 if not provided.

    Returns:
        float: The calculated area of the circle.
    """
    return pi * radius * radius
